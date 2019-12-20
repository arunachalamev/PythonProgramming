

def productExceptSelf(nums):
    left, right = 1,1
    leftPr, rightPr = [1],[1]
    i = 1
    while i< len(nums):
        left = left * nums[i-1]
        leftPr.append(left)
        i += 1
    
    j = len(nums)-1
    while j>0:
        right = right * nums[j]
        rightPr.append(right)
        j -= 1
    rightPr.reverse()

    print (leftPr,rightPr)

    ans = []
    for x,y in zip(leftPr,rightPr):
        ans.append(x*y)


    return ans


print (productExceptSelf([1,2,3,4]))