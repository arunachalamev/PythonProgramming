

def removePalindromeSub(s):
    if len(s) == 0: return 0
    if s[::] == s[::-1]: return 1
    return 2


print (removePalindromeSub('ababa')) #1
print (removePalindromeSub('abb')) #2


