# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:16:05 2017

@author: arellave
"""

from sklearn import datasets
import numpy as np
iris = datasets.load_iris()

iris_X = iris.data

# To createa missing values
masking_array = np.random.binomial(1,0.25,iris_X.shape).astype(bool)
iris_X[masking_array] = np.nan

#Replace missing value with mean
from sklearn import  preprocessing
impute = preprocessing.Imputer()
irix_X_prime = impute.fit_transform(iris_X)
print (irix_X_prime[:5])

#Replace missing value with median
impute = preprocessing.Imputer(strategy='median')
irix_X_prime = impute.fit_transform(iris_X)
print (irix_X_prime[:5])


#Consider missing value as -1 rather than nan
iris_X[np.isnan(iris_X)]=-1
print (iris_X[:5])
impute = preprocessing.Imputer(missing_values=-1)
irix_X_prime = impute.fit_transform(iris_X)
print (irix_X_prime[:5])


#Using pandas
import pandas as pd
iris_X[masking_array] = np.nan
iris_df = pd.DataFrame(iris_X,columns=iris.feature_names)
print (iris_df.fillna(iris_df.mean())['sepal length (cm)'].head(5))


