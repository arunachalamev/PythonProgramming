# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 08:24:01 2017

@author: arellave
"""

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


reg_data, reg_target = make_regression(n_samples=2000, n_features=3,effective_rank=2, noise=10)
lr = LinearRegression()

import numpy as np
n_bootstraps = 1000
len_data = len(reg_data)
subsample_size = np.int(0.75*len_data)
subsample = lambda: np.random.choice(np.arange(0,len_data),size = subsample_size)


coefs = np.ones((n_bootstraps,3))

for i in range(n_bootstraps):
    subsample_idx = subsample()
    subsample_X = reg_data[subsample_idx]
    subsample_y = reg_target[subsample_idx]
    lr.fit (subsample_X,subsample_y)
    coefs[i][0]=lr.coef_[0]
    coefs[i][1]=lr.coef_[1]
    coefs[i][2]=lr.coef_[2]
print ("Linear Regression :")
print (coefs)

    
r = Ridge()
n_bootstraps = 1000
len_data = len(reg_data)
subsample_size = np.int(0.75*len_data)
subsample = lambda: np.random.choice(np.arange(0,len_data),size = subsample_size)


coefs_r = np.ones((n_bootstraps,3))

for i in range(n_bootstraps):
    subsample_idx = subsample()
    subsample_X = reg_data[subsample_idx]
    subsample_y = reg_target[subsample_idx]
    r.fit (subsample_X,subsample_y)
    coefs_r[i][0]=r.coef_[0]
    coefs_r[i][1]=r.coef_[1]
    coefs_r[i][2]=r.coef_[2]
print ("Ridge Regression :")
print (coefs_r)

print ("Mean of coeff difference :")
print (np.mean(coefs- coefs_r, axis=0))

print ("Variance of coeff :")
print (np.var(coefs, axis=0))

print ("Variance of coeff_r :")
print (np.var(coefs_r, axis=0))
