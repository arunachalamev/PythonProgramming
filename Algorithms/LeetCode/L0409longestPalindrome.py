# Given a string which consists of lowercase or uppercase letters, 
# find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.


import collections

def longestPalindrome(s):
    res = 0
    oddExist = 0
    if len(s)<=1: return 1
    ch = set(s)

    count = collections.Counter(s)

    for c in ch:
        if count[c] % 2 == 0:
            res = res + count[c]
        if count[c] %2 != 0:
            res = res + int(count[c]-1)
            oddExist = 1

    return res+oddExist

def longestPalindrome2(s):
    odds = sum(v & 1 for v in collections.Counter(s).values()) # Calculate number of odd characters
    return len(s) - odds + bool(odds)

# assert (longestPalindrome('abccccdd') == 7)
# assert (longestPalindrome('ccc') == 3)

print (longestPalindrome2('cccddd'))
