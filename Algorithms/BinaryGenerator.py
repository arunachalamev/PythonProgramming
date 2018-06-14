# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:47:30 2017

@author: arellave
"""

#To generate Binary strings of given length
n=3
B = [-1]*n

def Binary(n):
    global B
    if (n<=0):
        print (B)
        return
    B[n-1]=0
    Binary(n-1)
    B[n-1]=1
    Binary(n-1)
    
Binary(n)