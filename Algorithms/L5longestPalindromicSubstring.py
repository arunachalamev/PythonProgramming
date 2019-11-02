def longestPalindromicSubstring (s):

    res = ''

    for i in range(len(s)):
        temp = helper(s,i,i)
        if len(temp) > len(res): res = temp
        temp = helper(s,i,i+1)
        if len(temp) > len(res): res = temp

    return res

def helper(s,l,r):
    while (l>=0 and r<len(s) and s[l]==s[r]):
        l = l-1
        r = r+1
    return s[l+1:r]


print(longestPalindromicSubstring("cbbd"))
