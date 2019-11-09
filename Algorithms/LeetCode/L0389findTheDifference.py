# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.

# Input:
# s = "abcd"
# t = "abcde"
# Output:
# e
# Explanation:
# 'e' is the letter that was added.

#OtherTechinque: Keep counter for character available in s using dictionary
# Scan through the character in t and look for non-existence

def findTheDifference(s,t):
    s=sorted(s)
    t=sorted(t)

    j=0

    while j<len(s):
        if s[j] == t[j]:
            pass
        else:
            return t[j]
        j= j+1

    return t[j]

print (findTheDifference("a","aa"))