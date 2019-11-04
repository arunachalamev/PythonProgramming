# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.


def numberOfSubarrays(nums, k):

    p = [-1]
    for i, v in enumerate(nums):
        if v & 1: p.append(i)   # add the position to p list when we encounter odd number
    p.append(len(nums))         # add the end position
    r = 0
    for i in range(1, len(p)-k):                # list p contains location of odd numbers, scan through it with k odd number
        r += (p[i]-p[i-1])*(p[i+k]-p[i+k-1])    # Multiply the combinations
    return r

print (numberOfSubarrays([1,1,2,1,1], k = 3))

