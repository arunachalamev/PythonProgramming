

def missingNumber(nums):
    l = len(nums)
    sumX = sum(nums)
    # print (l, sumX,l*(l+1)//2)
    return l*(l+1)//2 - sumX

print (missingNumber([9,6,4,2,3,5,7,0,1]))