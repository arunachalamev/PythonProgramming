# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:32:50 2017

@author: arellave
"""

import numpy as np
from sklearn import metrics
from sklearn.metrics import roc_auc_score

#Given x, y real value, generate the auc
y = np.array([1, 1, 2, 2])
pred = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
print ("AUC from Points:", metrics.auc(fpr, tpr))

#Given true and score value, generate the auc
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
print ("AUC from True and score value:", roc_auc_score(y_true, y_scores))

