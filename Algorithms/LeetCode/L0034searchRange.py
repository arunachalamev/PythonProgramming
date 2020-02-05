

def searchRange(nums,target):


    def modifiedBinarySearch (nums,target,leftBool):
        l, r = 0, len(nums)
        while l < r :
            mid = (l+r) //2
            if leftBool and nums[mid] == target or nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

    leftindex = modifiedBinarySearch(nums,target,True)
    rightindex = modifiedBinarySearch(nums,target, False)

    if leftindex == len(nums) or nums[leftindex] != target:
        return [-1,-1]
    return [leftindex, rightindex-1]


# print (searchRange([5,7,7,8,8,10],8))
# print (searchRange([5,7,7,8,8,10],1))
print (searchRange([2,2],3))
