# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 12:03:56 2017

@author: arellave
"""

def splitDataset(dataSet,axis,value):
    retDataset = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataset.append(reducedFeatVec)
    return retDataset

dataSet = [ [1, 6, 'yes'],
            [1, 7, 'yes'],
            [1, 6, 'no'],
            [0, 7, 'no'],
            [0, 6, 'no']]

splitDataset(dataSet,1,6)