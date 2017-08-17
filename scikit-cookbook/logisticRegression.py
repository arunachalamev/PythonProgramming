# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:42:49 2017

@author: arellave
"""

from sklearn.datasets import make_classification
X,y = make_classification(n_samples=1000,n_features=4)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()


X_train = X[:-200] # removes last 200 records
X_test = X[-200:] # removes first 200 records
y_train = y[:-200]
y_test = y[-200:]

lr.fit(X_train,y_train)
y_train_predictions = lr.predict(X_train)
y_test_predictions = lr.predict(X_test)

# print train and test accuracy
print (y_train_predictions == y_train).sum().astype(float) / y_train.shape[0]
print (y_test_predictions == y_test).sum().astype(float) / y_test.shape[0]


#Class imbalance
X,y = make_classification(n_samples=1000,n_features=4,weights=[0.95])
print sum(y)/(len(y)*1.)    # Only 5% positive class

X_train = X[:-500] 
X_test = X[-500:]
y_train = y[:-500]
y_test = y[-500:]

lr.fit(X_train,y_train)
y_train_predictions = lr.predict(X_train)
y_test_predictions = lr.predict(X_test)

# print train and test accuracy
print (y_train_predictions == y_train).sum().astype(float) / y_train.shape[0]
print (y_test_predictions == y_test).sum().astype(float) / y_test.shape[0]


# Looking at precision
print (y_test[y_test==1] == y_test_predictions[y_test==1]).sum().astype(float) / y_test[y_test==1].shape[0]


#sample re-weighting techinque
lr = LogisticRegression(class_weight={0:.15,1:.85})
lr.fit(X_train,y_train)

y_train_predictions = lr.predict(X_train)
y_test_predictions = lr.predict(X_test)

print (y_test[y_test==1] == y_test_predictions[y_test==1]).sum().astype(float) / y_test[y_test==1].shape[0]
print (y_test_predictions == y_test).sum().astype(float) / y_test.shape[0]


