

def breakPalindrome(palindrome):
    l = len(palindrome)
    for i in range(l//2):
        if palindrome[i] != 'a':
            return palindrome[:i] + 'a' + palindrome[i+1:]
    return palindrome[:-1]+'b' if l > 1 else ''

print (breakPalindrome('abccba'))