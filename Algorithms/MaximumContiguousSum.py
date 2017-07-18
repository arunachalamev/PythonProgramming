# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:14:50 2017

@author: arellave
"""



def MaxContSum(A):
    sum_ending_here = 0;
    max_sum_ending_here = 0;
    for i in A:
        sum_ending_here = sum_ending_here + i
        if sum_ending_here < 0:
            sum_ending_here = 0
            continue
        if max_sum_ending_here < sum_ending_here:
            max_sum_ending_here = sum_ending_here
    return max_sum_ending_here
   

A = [1,0,-3,5,-6,-7]
print "Maximum Contiguous sum in and array = " ,MaxContSum(A)


    