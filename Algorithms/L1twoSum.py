def twoSum(nums,target):
    seen = {}

    for i,v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return (seen[remaining] , i)
        seen[v] = i
    return None


print (twoSum([2, 7, 11, 15],9))