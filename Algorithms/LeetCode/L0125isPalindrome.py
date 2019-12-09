# Check for palindrome with only alphanumeric character

def isPalindrome(s):
    if len(s) == 0 : return True
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    i, j = 0, len(s)-1

    while (i<j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print (isPalindrome("A man, a plan, a canal: Panama"))
print (isPalindrome("race a car"))
