

def findDisappearedNumbers(nums):
    for x in  nums:
        if nums[abs(x)-1] > 0:
            nums[abs(x)-1] *= -1
    list = []
    for i,x in enumerate(nums):
        if x>0:
            list.append(i+1)

    return list

print (findDisappearedNumbers([4,3,2,7,8,2,3,1]))