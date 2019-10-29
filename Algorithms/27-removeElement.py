def removeElement(nums,val):
    length = len (nums)
    counter = 0
    for i in nums:
        if i == val:
            counter = counter + 1

    l , r = 0, len(nums) -1

    while (l<r):
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]
            r = r-1
        else:
            l = l +1
            
    return length-counter



print (removeElement([3,2,2,3],3))
print (removeElement([0,1,2,2,3,0,4,2],2))
