#  O(n) algorithm to determine if there exist increasing triplet in a given array
# Idea is to break array in to 3 segment using 2 threshold and find if there is a number in all segment
import math

def increasingTriplet(nums):
    threshold1 = math.inf
    threshold2 = math.inf

    for x in nums:
        if x <= threshold1:
            threshold1 = x
        elif x <= threshold2:
            threshold2 = x
        else:
            return True
    
    return False


print(increasingTriplet([1,2,3,4,5]))
print(increasingTriplet([5,4,3,2,1]))
print(increasingTriplet([5,5,1,0,8]))