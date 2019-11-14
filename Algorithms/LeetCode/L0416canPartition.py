# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.


def canPartition(nums):
    if sum(nums) % 2 != 0: return False
    possibleSums = {0}
    target = sum(nums) / 2

    for n in nums:
        possibleSums = possibleSums | {n + x for x in possibleSums}
        if target in possibleSums:
            return True

    return False


# Dp solution - 0/1 Knapsack Problem
# without optimization:
# If we dont pick num[i]: dp[i][j] = dp[i-1][j]
# If we pick nums[i]    : dp[i][j] = dp[i-1][j-nums[i]]

# with Optimization
def canPartition2(nums):
    target = int(sum(nums)/2)
    if sum(nums)%2 !=0: return False
    dp =[False]* (target+1)
    dp[0] = True

    for n in nums:
        i = target
        while i>0:
            if i>=n:
                dp[i] = dp[i] | dp[i-n]
            i = i -1
        print (dp)
    return dp[-1]


print (canPartition2([1, 5, 11, 5])) #True
print (canPartition2([1, 2, 3, 5]))  #False

