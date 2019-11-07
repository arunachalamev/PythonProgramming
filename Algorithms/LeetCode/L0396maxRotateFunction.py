
# Given an array of integers A and let n to be its length.
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1).

#O(n^2) algorithm
import math
def maxRotateFunction(A):
    maxsum = -math.inf
    if len(A) == 0: return 0
    for start in range(len(A)):
        i = start
        sum = 0
        for num in A:
            sum = sum + i*num
            i = i + 1
            if i >=len(A):
                i = 0
        maxsum = max(maxsum,sum)
    return maxsum

#O(N) Algorithm
def maxRotateFunction2(A):
    if len(A) == 0: return 0
    curr = sum([i*j for i,j in enumerate(A)])
    sumA = sum(A)
    lenA = len(A)
    maxsum = -math.inf
    while A:
        curr = curr + sumA - lenA*A.pop()
        maxsum = max (maxsum,curr)

    return maxsum


print (maxRotateFunction2([4,3,2,6]))
print (maxRotateFunction2([-2147483648,-2147483648]))