

# Parameter to tune for your needs
base_path = 'C:\\ML investigation helper\\Data\\' 
data_filename = 'toy example.csv'
fpr_threshold = 0.1
max_tree_depth = 4
use_date_in_filenames = False

# Parameters data scientists may want to tune.
# These values are good rules of thumb.
num_val_folds = 5  # If you have little data you may increase this value, e.g. to 20. Will have diminishing returns and at some point it will hit an upper abound (proportional to the size of your data).
test_size_base = 0.2  # quantile, 0.2 = 20%
log_C_max = 1  # log stands for base 10 logarithm.
log_C_min = -2
log_C_min_delta = 0.01
tree_min_samples_leaf = 3  # That's a regularization parameter of the explaining tree.

#%% Don't touch, unless you know what you're doing
import numpy as np
import pandas as pd
import random
import pickle
from copy import copy

import matplotlib.pyplot as plt
from datetime import date
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, roc_auc_score, roc_curve, recall_score, accuracy_score, confusion_matrix, f1_score, auc as calc_auc
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz

if use_date_in_filenames:
    todays_date = date.today()
    todays_date_str = '_' + todays_date.strftime('%Y_%m_%d')
else:
    todays_date_str = '' 
model_name = data_filename.split('.')[0].replace(' ','_')
model_filename = model_name+'_model' + todays_date_str
tree_filename = model_name+'_tree_model' + todays_date_str
fpr_tpr_pairs_filenames = model_name+'_fpr_tpr_pairs' + todays_date_str
roc_curve_filename = model_name+'_roc' + todays_date_str
feature_contribution_filename = model_name+'_feature_contribution' + todays_date_str

# CV parameters
hyper_opt_n_jobs = 1
#scorers = {'Accuracy': 'accuracy', 'Precision': 'precision', 'Recall': 'recall', 'AUC': 'roc_auc'}
score_funcs = {'precision': precision_score, 'AUC': roc_auc_score, 'recall': recall_score, 
    'accuracy': accuracy_score, 'confusion_matrix': confusion_matrix, 'F1': f1_score}

separator = '\t' if len(data_filename) >= 4 and data_filename[-4:] == '.tsv' else ','
df = pd.read_csv(base_path+data_filename, sep=separator)

# CV functions
def size_to_rel_size_and_len(size, input_len):
    if size >= 1: 
        len_ = copy.copy(size)
        size = size / input_len
    else:
        len_ = round(input_len * size)
    return size, len_

#%
def get_stratified_split(df, labels=None, seed=0):
    if labels is None:
        labels = set(df['label'])
    random.seed(seed)
    tr_ind = []
    test_ind = []
    for label in labels:
        cur_label_ind = list(df[df['label'] == label].index)
        random.shuffle(cur_label_ind)
        num_samples = len(cur_label_ind)
        test_size, test_len = size_to_rel_size_and_len(test_size_base, num_samples)
        if test_len + num_val_folds > num_samples:
            raise ValueError("Too few data points, insert at least %s of each label" % (int(np.ceil(num_val_folds / (1-test_size)))))
        test_ind.extend(cur_label_ind[-test_len:])
        tr_ind.extend(cur_label_ind[:-test_len])
    return tr_ind, test_ind

get_start = lambda x, length: x[:length]

def starts_with(input_str, prefix, apply_lower=True):
    if len(input_str) < len(prefix):
        return False
    else:
        start = input_str[:len(prefix)]
        if apply_lower:
            start = start.lower()
            prefix = prefix.lower()
        return start == prefix

print('--CV split--')
tr_ind, test_ind = get_stratified_split(df)
y = df['label']
x = df[[col for col in df.columns if not col == 'label' and not starts_with(col, 'ignore_')]]
x_tr_val = x.loc[tr_ind]
x_test = x.loc[test_ind]
y_tr_val = y.loc[tr_ind]
y_test = y.loc[test_ind]
skf = StratifiedKFold(num_val_folds,shuffle=True,random_state=0)

def get_classifier(log_C, x_tr, x_val, y_tr, y_val):
    scaler = StandardScaler().fit(x_tr)
    x_tr = scaler.transform(x_tr) #  x_tr is now np.array
    x_val = scaler.transform(x_val) #  x_val is now np.array
    model = LogisticRegression(C=10**log_C, random_state=0).fit(x_tr,y_tr)
    val_pred = model.predict_proba(x_val)
    return scaler, model, val_pred
        
def classifier_auc(log_C, x_tr, x_val, y_tr, y_val):
    _, _, val_pred = get_classifier(log_C, x_tr, x_val, y_tr, y_val)
    val_pred = val_pred[:,1]
    return roc_auc_score(y_val, val_pred)
        
def kfold_classifier_auc(skf, log_C, x, y):
    weighted_aucs = []
    for tr_ind, val_ind in skf.split(x, y):
        x_tr = x.iloc[tr_ind]
        y_tr = y.iloc[tr_ind]
        x_val = x.iloc[val_ind]
        y_val = y.iloc[val_ind]
        cur_auc = classifier_auc(log_C, x_tr, x_val, y_tr, y_val)
        weighted_aucs.append(cur_auc * len(val_ind))
    return sum(weighted_aucs) / y.shape[0]

print('--Training initial model--')
val_aucs = []
log_Cs = [log_C_min, (log_C_max + log_C_min) / 2, log_C_max]
for log_C in log_Cs:
    mean_val_auc = kfold_classifier_auc(skf, log_C, x_tr_val, y_tr_val)
    val_aucs.append(mean_val_auc)

print('--Tuning model--')
edges_max = max(val_aucs[0], val_aucs[2])
while log_Cs[2] - log_Cs[0] > log_C_min_delta and val_aucs[1] > edges_max:
    if val_aucs[2] > val_aucs[0]: #  If the max C is better then min C
        val_aucs[0] = val_aucs[1]
        log_Cs[0] = log_Cs[1]
    else:
        val_aucs[2] = val_aucs[1]
        log_Cs[2] = log_Cs[1]
    log_Cs[1] = (log_Cs[2] + log_Cs[0]) / 2
    print('Training with C = %.3f' % 10**log_Cs[1])
    edges_max = max(val_aucs[0], val_aucs[2])
print('Testing performance')
best_log_C = [C for C, auc in zip(log_Cs[::-1], val_aucs[::-1]) if auc == max(val_aucs)][0]
scaler, model, test_pred = get_classifier(best_log_C, x_tr_val, x_test, y_tr_val, y_test)
predict = lambda x: model.predict_proba(scaler.transform(x))

def prune_fpr_tpr_pair(fpr, tpr):
    fpr_tpr_pairs = []
    prev_fpr, prev_tpr = 0,0
    for (cur_fpr, cur_tpr) in zip(*(fpr,tpr)):
        if cur_fpr > prev_fpr:
            fpr_tpr_pairs.append((prev_fpr, prev_tpr))
        prev_fpr, prev_tpr = cur_fpr, cur_tpr
    if fpr_tpr_pairs[-1][0] < 1:
        fpr_tpr_pairs.append((1,1))
    return fpr_tpr_pairs  # list(zip(*fpr_tpr_pairs))

def limit_fpr_tpr(fpr, tpr, fpr_threshold):
    fpr_tpr_pairs = prune_fpr_tpr_pair(fpr, tpr)
    new_fpr, new_tpr = zip(*((cur_fpr, cur_tpr) for cur_fpr, cur_tpr in fpr_tpr_pairs if cur_fpr<=fpr_threshold))
    new_fpr = [0]+list(new_fpr)
    new_tpr = [0]+list(new_tpr)
    last_fpr, last_tpr = fpr_tpr_pairs[len(new_tpr)]
    tpr_edge_delta = (last_tpr - new_tpr[-1]) * (fpr_threshold - new_fpr[-1]) / (last_fpr - new_fpr[-1])
    new_tpr.extend([new_tpr[-1] + tpr_edge_delta]*2)
    new_fpr.extend([fpr_threshold, 1])
    return new_fpr, new_tpr

def norm_auc(fpr, tpr, fpr_threshold=1):
    full_area_auc = calc_auc(fpr,tpr)
    # ROI = Region Of Interest
    roi_area = full_area_auc - tpr[-1] * (1 - fpr_threshold)
    roi_random_area = (fpr_threshold ** 2) / 2
    roi_norm_area = (roi_area - roi_random_area) / (fpr_threshold - roi_random_area)
    return roi_area / fpr_threshold, roi_norm_area

print('Calculating performance metrics')
fpr, tpr, thresholds = roc_curve(y_test, test_pred[:,1])
fpr, tpr = limit_fpr_tpr(fpr, tpr, fpr_threshold)
auc, norm_auc = norm_auc(fpr, tpr, fpr_threshold)

feature_weight_sum = np.sum(np.abs(model.coef_[0,:]))
feature_importance_df = pd.DataFrame({
        'Feature name': x.columns, 
        'Importance (%)': 100 * np.round(model.coef_[0,:] / feature_weight_sum, 3), 
        'Correlation direction': ['Positive' if feature_coef > 0 else ('Zero' if feature_coef == 0 else 'Negative') for feature_coef in model.coef_[0,:]]},
    columns = ['Feature name', 'Importance (%)', 'Correlation direction'])

#%% Interpretability tree and display

def show_roc(fpr, tpr, fpr_threshold, auc, best_log_C, roc_curve_filename, base_path):
    fpr, tpr = zip(* ( (cur_fpr,cur_tpr) for cur_fpr, cur_tpr in zip(fpr, tpr) if cur_fpr <= fpr_threshold))
    plt.figure(figsize=(24,18))
    plt.title('ROC curve')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f, Normalized AUC = %0.2f, C = %0.3f' % (auc, norm_auc, 10**best_log_C))
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.05 * fpr_threshold,fpr_threshold * 1.05])
    plt.ylim([-0.05,1.05])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.savefig(base_path + roc_curve_filename + '.pdf')
#    plt.show()
    return

print('--Preparing data for explaining tree--')
tr_val_pred = predict(x_tr_val)
explain_data = []
for label in range(tr_val_pred.shape[1]):
    probs = tr_val_pred[:,label] 
    explain_data += [(x,label,prob) for x,prob in zip(x_tr_val.values, probs) if not prob == 0]
explain_x, explain_y, explain_weights = zip(*explain_data)
#[(x,0,1-prob) for x, prob in zip(x_tr_val.values, tr_val_pred) if prob < 1]+\
#    [(x,1,prob) for prob in tr_val_pred if prob > 0])

print('--Training explaining tree--')
explaining_tree = DecisionTreeClassifier(random_state=0, max_depth=max_tree_depth, min_samples_leaf=tree_min_samples_leaf)
explaining_tree.fit(explain_x, explain_y, sample_weight=explain_weights) #  test_pred is used because the
test_explain_pred = explaining_tree.predict_proba(x_test.values)
# goal is not to predict the correct labels, but to explain the predictions of
# the logistic regressor.
dot_graph = export_graphviz(explaining_tree, out_file=None, class_names=["benign", "malicious"], feature_names=list(list(x.columns)), impurity=True, filled=True)  #
graph = graphviz.Source(dot_graph)
#Image(graph.create_png())

#print("Copy and paste the tree description to: http://dreampuf.github.io/GraphvizOnline/\n  Description:\n"+dot_graph)
#  Alternative site: http://www.webgraphviz.com/
show_roc(fpr, tpr, fpr_threshold, auc, best_log_C, roc_curve_filename, base_path)
print("\n\nFeature importance and coefficients (linear model):")
print(feature_importance_df)

graph.view()

with open(base_path + model_filename + '.p','wb') as f:
    pickle.dump((scaler, model), f)
with open(base_path + tree_filename + '.p','wb') as f:
    pickle.dump(explaining_tree, f)
fpr_tpr_pairs = pd.DataFrame(list(zip(*(fpr, tpr)))[1:-1], columns=['FPR', 'TPR'])
fpr_tpr_pairs.to_csv(base_path + fpr_tpr_pairs_filenames+'.csv', index=False)
feature_importance_df.to_csv(base_path + feature_contribution_filename + '.csv', index=False)
print(fpr_tpr_pairs.head(20))
