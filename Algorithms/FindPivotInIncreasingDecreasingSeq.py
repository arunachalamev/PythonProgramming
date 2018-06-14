# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:57:20 2017

@author: arellave
"""

# Find the pivot value K in increasing and decreasing sequence

def main():
    A=[1,2,3,4,5,4,3,2,1,0,-1,-2]
    first = 0
    last = len(A) -1
    
    while (first <= last):
        if (first == last):
            print (A[first],first)
            return
        if (first == last -1):
            print ("Only two elements")
            print (first, last -1)
        mid = first + (last - first)/2
        if (A[mid]>A[mid+1] and A[mid-1] < A[mid]):
            print (mid, A[mid])
            return
        if (A[mid-1] < A[mid] and A[mid] < A[mid+1])
        




if __name__=="__main__":main()
