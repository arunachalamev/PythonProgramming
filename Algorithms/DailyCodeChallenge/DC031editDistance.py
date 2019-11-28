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

# using cache
def editDistance2(s1,s2):
    m,n = len(s1), len(s2)
    
    table = [[0]*(n+1) for _ in range(m+1)]

    for j in range(n+1):
        table[0][j] = j 
    for i in range(m+1):
        table[i][0] = i

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min (table[i-1][j-1], table[i-1][j], table[i][j-1])
    
    return table[-1][-1]


print (editDistance2("sitting","kitten"))