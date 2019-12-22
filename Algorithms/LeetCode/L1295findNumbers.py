

def findNumbers(nums):
    count = 0
    if len(nums) == 0: return 0
    for x in nums:
        if len(str(x))%2 == 0:
            count +=1
    return count


print(findNumbers([12,345,2,6,7896]))