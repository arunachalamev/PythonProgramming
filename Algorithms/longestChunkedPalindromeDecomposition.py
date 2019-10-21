def longestChunkedPalindromDecomposition(s):
    reverse_s = s[::-1]
    l = ''
    r = ''
    count = 0

    for i,j in zip(s,reverse_s):

        l = l+i 
        r = j+r

        if (l == r):
            count = count + 1
            l = ''
            r = ''
    
    return count

print (longestChunkedPalindromDecomposition('merchant'))