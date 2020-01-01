

def nextPermutation(nums):
    j = len(nums)-1

    while j>=1 and nums[j-1] > nums[j]:
            j -= 1
    # print (nums)

    if j == 0: 
        nums.reverse()
        return 

    start = j-1
    end = len(nums)-1
    while (nums[start] >= nums[end]):
        end -= 1
    # print (nums)

    nums[start], nums[end] = nums[end], nums[start]
    l, r = start+1, len(nums)-1
    (nums[l:r+1]).reverse()

    return nums

print (nextPermutation([1,2,3]))
print (nextPermutation([1,1]))

