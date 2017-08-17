# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:24:21 2017

@author: arellave
"""

from sklearn.datasets import make_regression
import numpy as np

reg_data, reg_target = make_regression(n_samples=200,n_features=500,n_informative=10,noise=2)

from sklearn.linear_model import Lars
lars = Lars(n_nonzero_coefs=10)
lars.fit(reg_data,reg_target)


print np.sum(lars.coef_ !=0)

train_n =100
lars_12 = Lars(n_nonzero_coefs=12)
lars_12.fit(reg_data[:train_n],reg_target[:train_n])

lars_500 = Lars()
lars_500.fit(reg_data[:train_n],reg_target[:train_n])

#Printing squared error 
print np.mean(np.power(reg_target[train_n:]-lars_12.predict(reg_data[train_n:]),2))
print np.mean(np.power(reg_target[train_n:]-lars_500.predict(reg_data[train_n:]),2))



#cross validation
from sklearn.linear_model import LarsCV
lcv = LarsCV()
lcv.fit(reg_data,reg_target)
print np.sum(lcv.coef_ !=0)
