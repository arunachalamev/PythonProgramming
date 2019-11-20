
#Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
#where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

# Input:
# [1,2,3]
# Output:
# 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]


def minMoves2(nums):
    nums.sort()

    targetIndex = int(len(nums)/2)
    target = nums[targetIndex]

    result = 0
    for x in nums:
        result = result + abs(x-target)


    return result

assert (minMoves2([1,2,3])== 2)
print (minMoves2([1,7,8,9]))

print ("done")