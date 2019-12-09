# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans

print (singleNumber([2,2,1]))
print (singleNumber([4,1,2,1,2]))
