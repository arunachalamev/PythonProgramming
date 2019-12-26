def maximumProduct(nums):
    nums = sorted(nums)
    n =  len(nums)-1

    return max(nums[0]*nums[1]*nums[n], nums[n]*nums[n-1]*nums[n-2])


print(maximumProduct([1,2,3]))
print(maximumProduct([1,2,3,4]))

