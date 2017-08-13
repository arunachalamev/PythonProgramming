# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 08:43:47 2017

@author: arellave
"""

from numpy import *

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines,4))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split(',')
        returnMat[index,:] = listFromLine[0:4]
        #classLabelVector.append(int(listFromLine[-1]))
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat,classLabelVector
    
    
    
returnMat, ClassLabelVector = file2matrix("iris.data")