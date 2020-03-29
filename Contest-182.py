import collections
def findLucky(arr):
    count = collections.Counter(arr)
    for x in sorted(count.keys(),reverse=True):
        if count[x] == x:
            return x
    return -1

# print (findLucky([2,2,3,4]))
# print (findLucky([1,2,2,3,3,3]))
# print (findLucky([2,2,2,3,3]))
# print (findLucky([5]))
# print (findLucky([7,7,7,7,7,7,7]))

from itertools import combinations
def numTeams(rating):
    ans = 0
    for x in list(combinations(rating,3)):
        if x[0]<x[1]<x[2]: ans +=1
        elif x[0] > x[1] > x[2]: ans +=1
    return ans

# print (numTeams([2,5,3,4,1]))
# print (numTeams([2,1,3]))
# print (numTeams([1,2,3,4]))


# def findGoodStrings(n,s1,s2,evil):

#     def nextword(s):
#         i = len(s) - 1
#         while s[i] == 'z' and i >=0:
#             i -= 1
#         s = s.replace(s[i], chr(ord(s[i])+1),1)
#         return s

#     print (nextword('aa'))
#     print(next(list('aa')))



