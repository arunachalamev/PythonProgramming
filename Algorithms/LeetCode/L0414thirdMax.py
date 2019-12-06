import math

def thirdMax(nums):
    first, second, third = -math.inf, - math.inf, -math.inf

    for x in nums:
        if x > first:
            third = second
            second = first
            first = x
        if second < x < first:
            third = second
            second = x
        if third < x < second:
            third = x

    if third == -math.inf:
            return first

    return third

print (thirdMax([3, 2, 1]))
print (thirdMax([1,2]))
print (thirdMax([2,2,3,1]))
print (thirdMax([1,-2147483648,2]))
