

def BSTOneChildPreOrderTraversal(nums):
    size = len(nums)
    for i in range(size-1):
        nextnums = nums[i] - nums[i+1]
        lastnums = nums[i] - nums[size-1]
        if nextnums*lastnums< 0:
            return False
    return True

print (BSTOneChildPreOrderTraversal([20,10,14,15,17]))
