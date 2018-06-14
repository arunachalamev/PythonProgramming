# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:00:26 2017

@author: arellave
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np

lr = LinearRegression()

boston = datasets.load_boston()

n_bootstraps = 1000
len_boston = len(boston.target)

subsample_size = np.int(0.5*len_boston)

#Lambda function
subsample = lambda:np.random.choice(np.arange(0,len_boston),size=subsample_size)

coefs = np.ones(n_bootstraps)

for i in range (n_bootstraps):
    subsample_idx = subsample()
    subsample_X = boston.data[subsample_idx]
    subsample_y = boston.target[subsample_idx]
    lr.fit(subsample_X,subsample_y)
    coefs[i] = lr.coef_[0]
    
import matplotlib.pyplot as plt
f = plt.figure(figsize=(7,5))
ax = f.add_subplot(111)
ax.hist(coefs,bins=50)
ax.set_title("Histogram of the lr.coef_[0].")

print (np.percentile(coefs,[2.5,97.5]))