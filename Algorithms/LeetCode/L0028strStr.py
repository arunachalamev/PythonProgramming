

def strStr(haystack, needle):
    n, L = len(haystack), len(needle)

    for i in range(n-L+1):
        if haystack[i:i+L] == needle:
            return i
    return -1

print (strStr('hello','ll'))
print (strStr('aaaaa','bba'))
