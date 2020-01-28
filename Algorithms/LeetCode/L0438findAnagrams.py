
import collections

def findAnagrams(s,p):
    l = len (p)
    result = []
    patterncount = collections.Counter(p)
    for i in range(len(s)-l):
        temp = s[i:i+l]
        srcCounter = collections.Counter(temp)
        if patterncount == srcCounter:
            result.append(i)
    return result
    
print (findAnagrams('cbaebabacd','abc'))