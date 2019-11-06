# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def maxNonAdjacementSum(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0],nums[1])
    if len(nums) == 3: return max(nums[0]+nums[2],nums[1])

    temp = nums.copy()
    sum_0 = temp[0] + maxNonAdjacementSum(temp[2:])
    sum_1 = temp[1] + maxNonAdjacementSum(temp[3:])

    return max(sum_0,sum_1)


# Linear time algorithm - O(N)
def maxNonAdjacementSum2(nums):
    previousInclusive = 0
    previousExclusive = 0

    for x in nums:
        temp = previousInclusive 
        previousInclusive = max(previousExclusive+x, previousInclusive)

        previousExclusive = temp

    return max(previousExclusive,previousInclusive) 


print (maxNonAdjacementSum2([2,4,6,2,5]))
print (maxNonAdjacementSum2([5,1,1,5,5]))
print (maxNonAdjacementSum2([4,1,1,4,2,1]))




