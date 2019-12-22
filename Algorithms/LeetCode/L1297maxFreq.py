
import collections

def maxFreq(s,maxLetters, minSize,maxSize):
    count =0
    mydict = collections.defaultdict(int)
    for i in range(minSize,maxSize+1):
        for x in range(len(s)-i+1):
            temp = s[x:x+i] 
            if len(set(temp)) <= maxLetters:
                mydict[temp] = mydict[temp] + 1

    if len(mydict) > 0:
        count = max(list(mydict.values()))
    else:
        count = 0
    return count

print (maxFreq('aababcaab',2,3,4))
print (maxFreq('aaaa',1,3,3))
print (maxFreq('aabcabcab',2,2,3))
print (maxFreq('abcde',2,3,3))
