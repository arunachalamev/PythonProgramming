# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:14:28 2017

@author: arellave
"""

def gcd(a,b):
    if a<b:
        temp = b
        b= a
        a = temp
    
    print a, b
    while (b!=0):
        a, b = b, a%b
    print "GCD:", a
    
gcd(4,12)
