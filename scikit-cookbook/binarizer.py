# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:32:59 2017

@author: arellave
"""
#Code to Binarize the feature/target/countinous value

from sklearn import datasets
import numpy as np
from sklearn import preprocessing

boston = datasets.load_boston()

#Similar to scaling, we have function and Class
#preprocessing.binarize
#preprocessing.Binarizer

new_target = preprocessing.binarize(boston.target, threshold= boston.target.mean())
print ("New Target after Binarization :")
print (new_target[:5])
print ("To Verify :")
print ((boston.target[:5]>boston.target.mean()).astype(int))

bin = preprocessing.Binarizer(boston.target.mean())
new_target = bin.fit_transform(boston.target)
print (new_target[:5])


#-----------------------------------------------
# special case for sparse matrix. threshold cannot be less than zero

from scipy.sparse import coo
spar = coo.coo_matrix(np.random.binomial(1,0.25,100))
#preprocessing.binarize(spar,threshold=-1)


#-------------------------------------------------
# working with categorical variable
iris = datasets.load_iris()
X= iris.data
y= iris.target

d = np.column_stack((X,y))

#convert text colum to 3 feature
text_encoder = preprocessing.OneHotEncoder()
print (text_encoder.fit_transform(d[:,-1:]).toarray()[:5])

#----------------------------------------------------
# DictVectorizer

from sklearn.feature_extraction import DictVectorizer
dv = DictVectorizer()
my_dict = [{'Species':iris.target_names[i]} for i in y]
print ("dic vectorizer :")
print (dv.fit_transform(my_dict).toarray()[:5])



#----------------------------------------------------
# Binarizing label features

from sklearn.preprocessing import LabelBinarizer
label_binarizer = LabelBinarizer()

new_target = label_binarizer.fit_transform(y)
print ("Label Binarizer shape :")
print (new_target.shape)
print (new_target[:5])
print (new_target[-5:])
print (label_binarizer.classes_)


label_binarizer.transform([3])