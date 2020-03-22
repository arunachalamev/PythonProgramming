
def createTargetArray(nums,index):
    target = list()
    for x,y in zip(nums,index):
        target.insert(y,x)
    return target

# print (createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
# print (createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
# print (createTargetArray(nums = [1], index = [0]))
import math
def sumFourDivisor(nums):
    def divisor(n):
        i, result = 1, []
        while i <= math.sqrt(n):
            if n%i == 0:
                if n/i == i:
                    result.append(i)
                else:
                    result.append(i)
                    result.append(n//i)
            i += 1
        return result
    total, temp = 0, []
    for x in nums:
        temp = divisor(x)
        if len(temp) == 4: 
            total += sum(temp)

    return total

# print (sumFourDivisor([21,4,7]))


# Failed attempts
def hasValidPath (grid):
    m,n = len(grid), len(grid[0])
    feasible = {1:[3,5], 2:[5,6], 3:[2,5,6], 4:[2,5,6], 5:[2,3,4], 6:[2,3,4] }
    d = {1:[0,1],  2:[1,0], 3:[1,1], 4:[0,1], 5:[-1,0], 6:[0,1]}
    i,j = 0,0
    
    while (i,j) != (m-1,n-1):
        direction = grid[i][j]
        i = i+ d[direction][0]
        j = j+ d[direction][1]
        if grid[i][j] not in feasible[direction]:
            return False

    return True
# print (hasValidPath([[2,4,3],[6,5,2]]))
# print (hasValidPath([[1,2,1],[1,2,1]]))
# print (hasValidPath([[1,1,2]]))
# print (hasValidPath([[1,1,1,1,1,1,3]]))
# print (hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))

def longestPrefix(s):
    if len(s) <=1 : return ''
    i,j = 0, len(s)-1
    prefix, suffix = '', ''
    while i<len(s) and j>0:
        prefix = prefix + s[i]
        i += 1
        suffix = s[j] + suffix 
        j -= 1
        if prefix == suffix:
            ans = prefix

    return ans

print (longestPrefix('level'))
print (longestPrefix('a'))
print (longestPrefix('leetcodeleet'))
print (longestPrefix('ababab'))


