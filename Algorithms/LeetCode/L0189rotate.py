

def rotate(nums, k):
    n = len(nums)
    nums[:] = nums[n-k:]+nums[:n-k]
    nums[:] = nums[-k:] + nums[:-k]
    return

def rotate2(nums,k):
    nums[:] = nums[::-1]
    A  = (nums[:k])[::-1]
    B = (nums[k:])[::-1]
    # print (A,B)
    return A + B

print (rotate2([1,2,3,4,5,6,7],3))
print (rotate2([-1,-100,3,99],2))
