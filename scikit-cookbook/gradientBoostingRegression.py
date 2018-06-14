# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:13:49 2017

@author: arellave
"""

from sklearn.datasets import make_regression
import numpy as np

X,y = make_regression(1000,2,noise=10)


from sklearn.ensemble import GradientBoostingRegressor as GBR

gbr = GBR()
gbr.fit(X,y)
gbr_preds = gbr.predict(X)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)
lr_preds = lr.predict(X)


gbr_residuals = y - gbr_preds
lr_residuals = y - lr_preds

print (np.percentile(gbr_residuals,[2.5,97.5]))
print (np.percentile(lr_residuals,[2.5,97.5]))

import matplotlib.pyplot as plt
f = plt.figure(figsize=(7,5))
ax = f.add_subplot(111)
ax.hist(gbr_residuals,bins=50,alpha=0.3,label="gbr")
ax.hist(lr_residuals,bins=50,alpha=0.3,label="lr")
ax.legend()

n_estimators = np.arange(100,1100,350)
gbrs = [GBR(n_estimators=i) for i in n_estimators ]
rediduals = {} # dictionary
for i, gbr in enumerate(gbrs):
    gbr.fit(X,y)
    print (gbr.n_estimators)
    #assigning key with value
    rediduals[gbr.n_estimators] = y - gbr.predict(X)


    