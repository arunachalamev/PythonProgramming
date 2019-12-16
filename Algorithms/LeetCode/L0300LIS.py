

def LIS(nums):
    if len(nums) == 0: return 0
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]> nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print (dp)
    return max(dp)

print (LIS([10,9,2,5,3,7,101,18]))