

def sortColors(nums):
    p0, curr = 0, 0
    p2 = len(nums)-1
    while curr <= p2:
        if nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        elif nums[curr] == 0:
            nums[curr], nums[p0] = nums[p0], nums[curr]
            p0 += 1
            curr += 1
        else:
            curr += 1

    return nums
print (sortColors([2,0,2,1,1,0]))
