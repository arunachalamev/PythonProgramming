# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 09:12:13 2017

@author: arellave
"""

#from sklearn import datasets
import sklearn.datasets as d
import numpy as np

#print datasets.load_*?

#Loading a dataset

boston = d.load_boston()
print boston.DESCR

housing = d.fetch_california_housing()
print housing.DESCR

X, y = boston.data, boston.target

#print datasets.make_*?

#Creating a Dataset
reg_data = d.make_regression()
complex_reg_data = d.make_regression(1000,10,5,2,1.0)
print complex_reg_data[0].shape

classification_set = d.make_classification(weights=[0.1])
np.bincount(classification_set[1])


blobs = d.make_blobs()
