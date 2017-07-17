# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:58:04 2017

@author: arellave
"""

#Longest Increasing subsequence in an array


def LongestIncreasingSubsequence(A):
    x=len(A)
    LIS=[]
    LIS.append(1 if A[0]>0 else 0)
    for i in range(1,x):
        maximum = 0
        ans = 0
        for j in range(0,i):
#            print "i=",i,"j=",j,"LIS[",j,"]=",LIS[j]
            maximum = max(maximum,LIS[j])
            if (A[i]>A[j]):
                ans = maximum + 1
            else:
                ans =LIS[i-1] 
        LIS.append(ans)
    print LIS
    

A=[1,2,1,4,0,6]
LongestIncreasingSubsequence(A)


A=[-1,-2,-1,-4,-0,-6]
LongestIncreasingSubsequence(A)
