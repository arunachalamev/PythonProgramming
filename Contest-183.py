def minSubsequence(nums):
    tot = sum(nums)
    temp = sorted(nums, reverse = True)
    # print (tot,temp)
    result = []
    prefix = 0
    for x in temp:
        prefix += x
        remainingTot = tot - prefix
        result.append(x)
        if remainingTot < prefix:
            break
        # print (prefix,remainingTot)
    return result

# print (minSubsequence([4,3,10,9,8]))
# print (minSubsequence([4,4,7,6,7]))
# print (minSubsequence([6]))


def numSteps(s):
    x = int(s,2)
    count = 0
    while x>1 :
        if x %2 == 0:
            x = x//2
        else:
            x = x + 1
        count += 1
    return count

# print (numSteps('1101'))
# print (numSteps('10'))
# print (numSteps('1'))
# print (numSteps("1111011110000011100000110001011011110010111001010111110001"))
import re
def longestDiverseString(a,b,c):
    d = {'a':a, 'b':b, 'c':c}
    d = sorted(d.items(), reverse=True, key = lambda x: x[1])
    s = []
    for k,v in d:
        s += ([k]*v)
    s = ''.join(s)
    # print (s)
    if 'aaa' not in s and 'bbb' not in s and 'ccc' not in s:
        return s
    i=2
    j=len(s)-1
    s = list(s)
    while i<j:
        s[i], s[j] = s[j], s[i]
        i += 3
        j -= 1
    s= ''.join(s)
    s = re.sub('a{3,}','aa',s)
    s = re.sub('b{3,}','bb',s)
    s = re.sub('c{3,}','cc',s)

    return s

# print (longestDiverseString(a = 1, b = 1, c = 7))
# print (longestDiverseString(a = 2, b = 2, c = 1))
# print (longestDiverseString(a = 7, b = 1, c = 0))
print (longestDiverseString(a = 1, b = 3, c = 5))


