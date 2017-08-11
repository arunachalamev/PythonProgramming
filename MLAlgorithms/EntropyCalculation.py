# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:48:48 2017

@author: arellave
"""

#Calculating entropy of a vector

import math
X1 = [1,1,1,1,1]
X2 = [1,0,1,0,1,0,1,0,1,0]

def entropy(data):
    count0, count1 = 0,0
    for i in range(len(data)):
        if data[i]==0: count0 += 1
        else: count1 += 1
    p0,p1 = count0*1.0/len(data),count1*1.0/len(data)
    v0 = math.log(p0,2) if p0!=0 else 0
    v1 = math.log(p1,2) if p1!=0 else 0
    print -p0*v0 - p1*v1
    return

entropy(X1)
entropy(X2)