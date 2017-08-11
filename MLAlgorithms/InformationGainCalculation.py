# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:20:05 2017

@author: arellave
"""

#Calculates the Information gain

import math
X1 = [1,1,1,1,1,0,0,0,0,0]
X2 = [1,0,1,0,1,0,1,0,0,0]

label = [1,1,1,1,1,0,0,0,0,0]

def entropy(data):
    count0, count1 = 0,0
    for i in range(len(data)):
        if data[i]==0: count0 += 1
        else: count1 += 1
    p0,p1 = count0*1.0/len(data),count1*1.0/len(data)
    v0 = math.log(p0,2) if p0!=0 else 0
    v1 = math.log(p1,2) if p1!=0 else 0
    return -p0*v0 - p1*v1
    

def information_gain(feature,label):
    f0=[]
    f1=[]
    c0=[]
    c1=[]
    for i in range(len(label)):
        if feature[i] == 0:
            c0.append(float(label[i]))
            f0.append(float(feature[i]))
        else:
            c1.append(float(label[i]))
            f1.append(float(feature[i]))
    x = entropy(label)
    y = len(f0)*1.0/len(feature)*entropy(c0)
    z = len(f1)*1.0/len(feature)*entropy(c1)
    print x-y-z
    
information_gain(X1,label)
information_gain(X2,label)
