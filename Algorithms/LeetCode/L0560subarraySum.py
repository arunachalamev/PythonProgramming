import collections

def subarraySum(nums,k):
    count =  collections.Counter()
    count[0]= 1
    ans,sum = 0, 0
    for n in nums:
        sum = sum + n
        ans = ans + count[sum-k]
        count[sum] += 1
    return ans

print (subarraySum([1,1,1],2))
print (subarraySum([1,2,3],3))
