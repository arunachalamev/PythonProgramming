# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:39:42 2017

@author: arellave
"""

from sklearn import preprocessing
import sklearn.datasets as d
import numpy as np
import scipy


#load boston dataset
boston = d.load_boston()
X, y = boston.data, boston.target

print X[:,:3].mean(axis=0)
print X[:,:3].std(axis=0)

#Scaling via function
X_2 = preprocessing.scale(X[:,:3])
print X_2.mean(axis=0)
print X_2.std(axis=0)

# Normalizing vis class
my_scaler = preprocessing.StandardScaler()
my_scaler.fit(X[:,:3])
print my_scaler.transform(X[:,:3]).mean(axis=0)


#Min max Normalizer
my_minmax_scaler = preprocessing.MinMaxScaler()
my_minmax_scaler.fit(X[:,:3])
print my_minmax_scaler.transform(X[:,:3]).max(axis=0)


#To Change Min Max value other than 0 and 1
my_odd_scaler = preprocessing.MinMaxScaler(feature_range = (-3.14,3.14))

#Normalizing the sample to unit length
normalized_X = preprocessing.normalize(X[:,:3])
print "normalized X: ",normalized_X


#identity transformation
my_useless_scaler = preprocessing.StandardScaler(with_mean=False,with_std=False)
transform_sd = my_useless_scaler.fit_transform(X[:,:3]).std(axis=0)
original_sd = X[:,:3].std(axis=0)

print "Array Equal:"
print np.array_equal(transform_sd,original_sd)

matrix=scipy.sparse.eye(1000)
#preprocessing.scale(matrix)
preprocessing.scale(matrix,with_mean=False)