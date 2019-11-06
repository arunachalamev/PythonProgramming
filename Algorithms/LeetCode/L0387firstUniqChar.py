
# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

from  collections import Counter

def firstUniqChar(s):

    count = Counter(s)

    for i,ch in enumerate(s):
        if count[ch] == 1:
            return i
    
    return -1


print (firstUniqChar('leetcode'))
print (firstUniqChar('loveleetcode'))

