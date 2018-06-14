# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:18:48 2017

@author: arellave
"""
#%%
n =10
Fib=[]

Fib.append(0)
Fib.append(1)
Fib.append(1)

for i in range(3,n+1):
    FirstElement = Fib[i-2]
    SecondElement = Fib[i-1]
    Fib.append(FirstElement+SecondElement)

print (Fib)
#%%