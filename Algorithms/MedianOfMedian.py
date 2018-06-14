# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%

def median_of_medians(A,i):
#    print "Length: ", len(A) 
#    print "Range:  ", range (0,len(A),5)  
    
    sublists = [A[j:j+5] for j in range(0,len(A),5)]
#    print "Sublist:", sublists
    
    medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]
#    print "medians:", medians
    
    if len(medians) <=5:
        pivot = sorted(medians)[len(medians)/2]
       
    else:
        pivot = median_of_medians(medians,len(medians)/2)
 
    low = [j for j in A if j < pivot]       
    high = [j for j in A if j > pivot]
    
#    print "pivot:", pivot
#    print "low:  ", low
#    print "high: ", high

    k = len(low)
#    print "k: ",k
    if i<k:
        return median_of_medians(low,i)
    elif i>k:
        return median_of_medians(high,i-k-1)
    else:
        return pivot
        
# Assumption: Input array needs to be unique
A = [1,2,3,4,5,1000,8,9]

print (A)
#To print smallest element
for i in range (0,len(A)):
    print (median_of_medians(A,i))    
    print  ("<<<---- ", i ," th smallest element ")
    
#To Print largest element
for i in range (0,len(A)):
    x = len(A) - i -1
    print (median_of_medians(A,x))    
    print  ("<<<---- ", i ," th largest element ")

        
#%%

