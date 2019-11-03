def countSmaller(nums):
    nums.reverse()
    n = len(nums)
    if n <=0 : return []
    result = [0]*len(nums)
    result[0] = 0
    for i in range(1,n):
        j = i -1
        while (nums[j]>= nums[i] and j >=0):
            j = j - 1
        if j >= 0: result[i] = result[j] + 1
    result.reverse()

    return (result)





# print(countSmaller([5,2,6,1]))
print(countSmaller([2,0,1]))
# print(countSmaller([-1,-1]))

