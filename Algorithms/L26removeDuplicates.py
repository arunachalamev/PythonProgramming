# Two pointer mechanism to remove duplicates in-place (without extra memory)
def removeDuplicates(nums):
    l,r =0,1

    while (r<len(nums)):
        if nums[l] == nums[r] : r= r+1
        else:
            l = l+1
            nums[l] = nums[r]
            r = r+1
    return l+1,nums



print (removeDuplicates([1,1,2]))
print (removeDuplicates([0,0,1,1,1,2,2,3,3,4]))