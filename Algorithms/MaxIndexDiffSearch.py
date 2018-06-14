# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:05:45 2017

@author: arellave
"""

#Given the the Array, find the max j-i such that A[j] > A[i]

def main():
    A=[14,3,9,0,8]
    Min = [0]*len(A)
    Max = [0]*len(A)
    
    Min[0]=A[0]
    Max[len(A)-1]=A[-1]
    
    for i in range(1,len(A)):
        Min[i] = min(A[i],Min[i-1])
    
    for j in range(len(A)-2,-1,-1):
        Max[j] = max(A[j],Max[j+1])

    print (Min)
    print (Max)
    i,j,Diff=0,0,-1
#    print i,j
    while (i<len(A) and j <len(A)):
        if (Min[i]<Max[j]):
            Diff = max(Diff, j-i)
#            print i,j,Diff            
            j = j+1
        else:
            i = i+1
            
    print (Diff)

if __name__ == "__main__": main()


