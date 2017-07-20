# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 20:04:01 2017

@author: arellave
"""
#%%
def main():
    k,n = 2,10
    print exponential(k,n)
    
def exponential(k,n):
    if (n==0): 
        return 1
    if (n%2 == 0):
        a = exponential(k,n/2)
        return a*a        
#        return exponential(k,n/2)*exponential(k,n/2)
    if (n%2==1):
        a = exponential(k,n-1)
        return k*a
#        return k*exponential(k,n-1)

if __name__ == "__main__": main()
   
#%%