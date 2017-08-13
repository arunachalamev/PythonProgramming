# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:28:27 2017

@author: arellave
"""

from math import log

def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts ={}
    for featureVec in dataset:
        currentLabel= featureVec[-1]
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] +=1
        
    shannonEntropy = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEntropy -= prob * log(prob,2)
    return shannonEntropy


def createDataSet():
    dataSet = [ [1, 1, 'maybe'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels


myData, labels = createDataSet()
print calcShannonEnt(myData)

        