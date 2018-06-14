# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:09:51 2017

@author: arellave
"""

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    print (dataSet.min(0))
    print (dataSet.max(0))
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    print (m)
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals
    
Normalized,Range, MinValues = autoNorm(returnMat)
