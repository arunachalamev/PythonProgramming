


def isAlienSorted(words, order):

    def compare(s1,s2,order):
        i,j = 0, 0
        Flag = False
        while i<len(s1) and j<len(s2) and s1[i] == s2[j]:
            i += 1
            j += 1
            Flag = True
        
        if Flag == True:
            if i >= len(s1):
                return True
            else:
                return False

        if order.find(s1[i]) < order.find(s2[j]):
            return True
        
        return False

    for i in range(1,len(words)):
        s1 = words[i-1]
        s2 = words[i]
        if compare(s1,s2,order) == False:
            return False
    
    return True

print (isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))
print (isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz"))
print (isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz"))

