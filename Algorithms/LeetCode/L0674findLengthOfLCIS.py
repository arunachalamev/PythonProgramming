

def findLengthOfLCIS(nums):
    current = float('-inf')
    maxLength, length = 0, 0
    for x in nums:
        if current<x:
            length +=1
        else:
            length = 1
        maxLength = max(maxLength,length)
        current = x

    return maxLength

print (findLengthOfLCIS([1,3,5,4,7]))
print (findLengthOfLCIS([2,2,2,2]))
print(findLengthOfLCIS([1,3,5,7]))
print(findLengthOfLCIS([1,3,5,4,2,3,4,5]))
print(findLengthOfLCIS([2,1,3]))
