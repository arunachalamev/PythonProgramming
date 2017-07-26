# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 08:50:30 2017

@author: arellave
"""

#Calculate the GCD to overcome the problem of above range
def GCD(a,b):
    if a<b:
        temp = b
        b= a
        a = temp
    
    while (b!=0):
        a, b = b, a%b
    return a


def LCM(a,b):
    if (a>b): 
        temp = a/GCD(a,b)
        return b*temp
    else: 
        temp = b/GCD(a,b)
        return a*temp
    
print LCM(10,20)
print LCM(10,10)
print LCM(3,4)