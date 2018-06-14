# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:34:05 2017

@author: arellave
"""

from sklearn import datasets
iris = datasets.load_iris()
iris_X = iris.data


from sklearn import decomposition
pca = decomposition.PCA()
print (pca)

# Each columns of the new matrix is orthogonal
iris_pca = pca.fit_transform(iris_X)
print ("Principal components :")
print (iris_pca[:5])

print ("Explained variance :")
print (pca.explained_variance_ratio_)

#Reducing the dimension
pca = decomposition.PCA(n_components = 2)
iris_X_prime = pca.fit_transform(iris_X)

print ("Dimension reduced shape :")
print (iris_X_prime.shape)

print ("Summed up explained variance :")
print (pca.explained_variance_ratio_.sum())


#To reduce based on the variance explained
pca = decomposition.PCA(n_components = 0.98)
iris_X_prime = pca.fit_transform(iris_X)

print ("Dimension reduced shape :")
print (iris_X_prime.shape)

print ("Summed up explained variance :")
print (pca.explained_variance_ratio_.sum())



#Factor Analysis
from sklearn.decomposition import FactorAnalysis
fa = FactorAnalysis(n_components = 2)
iris_2d = fa.fit_transform(iris.data)
print ("Two components of Factor Analysis :")
print (iris_2d[:5])
