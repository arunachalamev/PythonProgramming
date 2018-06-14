# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:23:52 2017

@author: arellave
"""

#%%
#Median of two sorted list

def main():
    First = range(0,5)
    Second = range(5,10)
#    print A,B
#    print "Start of Main:"
    print (median(First,Second))
#    print "End of Main"    
    
def median(A,B):
    if len(A) == 2 & len(B) == 2 :
        Median = (max(A[0],B[0]) + min(A[1],B[1]))/2.0
#        print Median
        return Median
        
    FirstArrayMid = len(A)/2
    SecondArrayMid = len(B)/2
    
    m1 = A[FirstArrayMid]
    m2 = B[SecondArrayMid]
#    print FirstArrayMid, SecondArrayMid
    if m1 == m2:
        print (m1)
        return m1
        
    if m1 > m2:
        indexOfm1 = A.index(m1) + 1
        A = A[0:indexOfm1]
        indexOfm2 = B.index(m2)
        B = B[indexOfm2:]
        return median(A,B)
        
    if m1 < m2:
        indexOfm1 = A.index(m1)
        A = A[indexOfm1:]
        indexOfm2 = B.index(m2) + 1
        B = B[0:indexOfm2]
        return median(A,B)
    

if __name__ == "__main__": main()


#%% 