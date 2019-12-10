

def maxSubArray(nums):
    maxSum = curSum = nums[0]
    for i in range(1,len(nums)):
        curSum = max(nums[i],curSum+nums[i])
        maxSum = max(curSum,maxSum)
    return maxSum

print (maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


def maxSubArrayDP(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1] 
        max_sum = max(nums[i], max_sum)
    return max_sum