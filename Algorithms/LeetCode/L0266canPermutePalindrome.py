
import collections
def canPermutePalindrome(s):
    counter = collections.Counter(s)
    flag =0
    if len(counter) == 1: return True
    G = []
    for ch in s:
        if ch not in G: G.append(ch)
    for x in G:
        if counter[x] %2 == 1 and flag ==1:
            return False
        if counter[x] %2 ==1:
            flag = 1
    return True

print(canPermutePalindrome(''))
