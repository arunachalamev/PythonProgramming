# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 08:39:01 2017

@author: arellave
"""

from sklearn.datasets import make_regression
import numpy as np
reg_data, reg_target = make_regression(n_samples=100,n_features=2,effective_rank=1, noise=10)

from sklearn.linear_model import RidgeCV
rcv = RidgeCV(alphas=np.array([0.1,0.2,0.3,0.4]))
#print rcv
rcv.fit(reg_data,reg_target)
print rcv.alpha_

rcv2 = RidgeCV(alphas=np.array([0.08,0.09,0.1,0.11,0.12]))
#print rcv2
rcv2.fit(reg_data,reg_target)
print rcv2.alpha_


alphas_to_test = np.linspace(0.01,1)
rcv3 = RidgeCV(alphas = alphas_to_test,store_cv_values= True)
rcv3.fit(reg_data,reg_target)


print rcv3.cv_values_.shape


smallest_idx = rcv3.cv_values_.mean(axis=0).argmin()
print alphas_to_test[smallest_idx]
print rcv3.alpha_

#with different scorer

def MAD(target, prediction):
    absolute_deviation = np.abs(target-prediction)
    return absolute_deviation.mean()
    
import sklearn
MAD = sklearn.metrics.make_scorer(MAD,greater_is_better=False)
rcv4 = RidgeCV(alphas=alphas_to_test,store_cv_values=True,scoring=MAD)
rcv4.fit(reg_data,reg_target)

smallest_idx = rcv4.cv_values_.mean(axis=0).argmin()
print alphas_to_test[smallest_idx]