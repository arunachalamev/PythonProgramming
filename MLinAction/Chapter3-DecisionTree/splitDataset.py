# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 12:03:56 2017

@author: arellave
"""

from shannonEntropy import *

def splitDataset(dataSet,axis,value):
    retDataset = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataset.append(reducedFeatVec)
    return retDataset




def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataset = splitDataset(dataSet,i,value)
            prob = len(subDataset)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataset)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature



dataSet = [ [0, 1, 'yes'],
            [0, 1, 'yes'],
            [0, 0, 'no'],
            [0, 0, 'no'],
            [0, 0, 'no']]

#splitDataset(dataSet,1,6)

print (chooseBestFeatureToSplit(dataSet))
