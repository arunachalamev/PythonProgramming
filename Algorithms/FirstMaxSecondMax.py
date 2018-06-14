# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:35:39 2017

@author: arellave
"""

# O(n) Algorithm to calculate first and second max from the array

def main():
    A=[-1,-2,-3,-4, 5]
    
    Max = A[0]
    for i in range (1, len(A)):
        if Max < A[i]:
            Max = A[i]
    print (Max) 


    FirstMax = max(A[0],A[1])
    SecondMax = min (A[0],A[1])
    
    for i in range (2, len(A)):
        if A[i] > FirstMax:
            SecondMax = FirstMax
            FirstMax = A[i]
        elif A[i] > SecondMax:
            SecondMax = A[i]
    
    print (FirstMax, SecondMax)

if __name__ == "__main__": main()
