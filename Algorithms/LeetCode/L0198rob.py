

def rob(nums):
    if len(nums) ==0: return 0
    if len(nums) ==1: return nums[0]
    if len(nums) == 2: return max(nums[0],nums[1])

    prevPrev, prev = 0, 0
    for index,value in enumerate(nums):
        current = max(prev, prevPrev+value)
        prevPrev= prev
        prev= current
    return current


print(rob([2,7,9,3,1]))