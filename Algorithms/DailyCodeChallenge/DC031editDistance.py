# The edit distance between two strings refers to the minimum number of character insertions, 
# deletions, and substitutions required to change one string to the other. 
# For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, 
# substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

def editDistance(s1,s2):
    if s1 == s2: return 0
    if not s1: return len(s2)
    if not s2: return len(s1)
    if s1[0] == s2[0]: return editDistance(s1[1:],s2[1:])
    return 1 + min (editDistance(s1[1:],s2) , editDistance(s1,s2[1:]), editDistance(s1[1:],s2[1:]))

print (editDistance("sitting","kitten"))