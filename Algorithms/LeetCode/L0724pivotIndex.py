


def pivotIndex(nums):
    sumX = sum(nums)
    if len(nums) <3: return -1
    if sum(nums[1:])==0: return 0

    leftSum = 0
    rightSum = sumX - nums[0]
    if leftSum == rightSum : return 0
    for index in range(1,len(nums)):
        leftSum += nums[index-1] 
        rightSum -= nums[index]
        if leftSum == rightSum:
            return index
    if sum(nums[:-1])==0: return len(nums)-1  
    return -1

# def pivotIndex2(nums):
#     if sum(nums[1:])==0: return 0
#     if sum(nums[:-1])==0: return len(nums)
#     for i in rage(nums):
#         if sum(nums[:])

print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
print(pivotIndex([-1,-1,-1,0,1,1]))
print(pivotIndex([-1,0,1,-1]))
print(pivotIndex([-1,-1,0,1,1,0]))
print(pivotIndex([-1,-1,1,1,0,0]))


