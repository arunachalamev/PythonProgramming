# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:34:13 2017

@author: arellave
"""

from sklearn import datasets
boston = datasets.load_boston()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(boston.data,boston.target)

predictions = lr.predict(boston.data)

print ("Printing Coefficient :")
print (lr.coef_)

print ("Coefficient along with feature Name :")
print (zip(boston.feature_names,lr.coef_))


#Fitting by normalizing the data
lr2 = LinearRegression(normalize= True)
lr2.fit(boston.data,boston.target)
preiction2 = lr2.predict(boston.data)

print ("Coefficient along with feature Name :")
print (zip(boston.feature_names,lr2.coef_))


#Plotting the residuals
import matplotlib.pyplot as plt
import numpy as np
f= plt.figure(figsize=(7,5))
ax = f.add_subplot(111)
ax.hist(boston.target-predictions,bins=50)
ax.set_title("Histogram of Residuals")

print ("Mean of residuals :")
print (np.mean(boston.target-predictions))


#plotting q-q plot
from scipy.stats import probplot
f= plt.figure(figsize=(7,5))
ax = f.add_subplot(111)
probplot(boston.target-predictions,plot=ax)



def MSE(target, predictions):
    squared_deviation = np.power(target-predictions,2)
    return np.mean(squared_deviation)
    
    
def MAD(target,predictions):
    absolute_deviation = np.abs(target-predictions)
    return np.mean(absolute_deviation)
    
print ("Mean squared Error :")
print (MSE(boston.target,predictions))

print ("Mean Absolute Error :")
print (MAD(boston.target,predictions))

