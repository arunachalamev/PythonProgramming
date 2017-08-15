# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:33:26 2017

@author: arellave
"""

#use of inbuilt pipeline.

from sklearn import datasets
import numpy as np
# generate random symmetric psd matrix
mat = datasets.make_spd_matrix(10)
masking_array = np.random.binomial(1,0.1,mat.shape).astype(bool)
mat[masking_array]= np.nan
print mat[:4,:4]


#without pipeline
from sklearn import preprocessing
impute = preprocessing.Imputer()
scaler = preprocessing.StandardScaler()
mat_imputed = impute.fit_transform(mat)
print "Imputing :"
print mat_imputed[:4,:4]

mat_imp_and_scaled = scaler.fit_transform(mat_imputed)
print "Scaling :"
print mat_imputed[:4,:4]


#using pipeline
from sklearn import pipeline
pipe = pipeline.Pipeline([('impute',impute),('scaler',scaler)])

print pipe

new_mat = pipe.fit_transform(mat)
print "Pipeline Mat:"
print new_mat[:4,:4]

print np.array_equal(new_mat,mat_imp_and_scaled)



#inverse transform for scaler
print "Inverse Transform of Scaler:"
print scaler.inverse_transform(new_mat)[:4,:4]
