# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:43:40 2017

@author: arellave
"""

from sklearn.datasets import make_regression
import numpy as np

reg_data, reg_target = make_regression(n_samples=200,n_features=500,n_informative=5,noise=5)

from sklearn.linear_model import Lasso
lasso = Lasso()

lasso.fit(reg_data,reg_target)

# prints the number of non zero coefficient
print np.sum(lasso.coef_ !=0)

# if alpha parameter is 0, then linear regression
lasso_0 = Lasso(alpha=0)
lasso_0.fit(reg_data,reg_target)
print np.sum(lasso_0.coef_ != 0)

#Cross Validation to choose best alpha(lambda) parameter
from sklearn.linear_model import LassoCV
lassocv = LassoCV()
lassocv.fit(reg_data,reg_target)

#prints the alpha and coefficient
print lassocv.alpha_
print lassocv.coef_[:5]
print np.sum(lassocv.coef_ !=0)


#To use it as a feature selection
mask = lassocv.coef_ != 0
new_reg_data = reg_data[:, mask]
print new_reg_data.shape

