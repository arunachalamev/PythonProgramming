

def maxSubArrayLen(nums,k):
    acc,ans = 0, 0
    mapping = {0:-1}
    for i,v in enumerate(nums):
        acc = acc + v
        if acc not in mapping:
            mapping[acc] = i
        if acc-k in mapping:
            ans = max(ans,i-mapping[acc-k])
    return ans

print (maxSubArrayLen([1, -1, 5, -2, 3],3))
