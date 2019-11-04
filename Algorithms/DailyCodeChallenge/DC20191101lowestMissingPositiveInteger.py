# O(n) algorithm to find the lowest missing positive number given an Integer array

def lowestMissingPositiveIngeter(nums):

    m = 1
    temp = []

    for x in nums:
        if m<x and x >0:
            temp.append(x)
        
        elif m == x:
            m = m + 1
            while (temp.count(m)):
                temp.remove(m)
                m = m + 1
    
    return m

print (lowestMissingPositiveIngeter([2,1,0]))
print (lowestMissingPositiveIngeter([3,4,-1,1]))

