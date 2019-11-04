# Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by 
# an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array 
# by any possible subset and multiplicand.

# Return True if the array is good otherwise return False.

from fractions import gcd
from functools import reduce

def gcd_1(a,b):
    if a<b: a,b = b,a
    while b>0:
        a,b = b, a%b
    return a

def isGoodArray(nums):

    return reduce(gcd_1,nums) == 1

print (isGoodArray([12,5,7,23]))
print (isGoodArray([29,6,10]))
print (isGoodArray([3,6]))

print (gcd_1(10,9))