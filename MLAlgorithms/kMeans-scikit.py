# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

from sklearn.cluster import KMeans
from sklearn import datasets
from pylab import *

iris = datasets.load_iris()

X,y = iris.data, iris.target

k_means = KMeans(n_clusters=3,random_state=0)

k_means.fit(X)

y_pred = k_means.predict(X)
scatter (X[:,0],X[:,1],c=y_pred)
show()

#%%