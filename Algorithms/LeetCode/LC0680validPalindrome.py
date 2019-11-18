# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.


def validPalindrome(s):
    if not s : return True
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            string1 = s[left:right]
            string2 = s[left+1 : right+1]

            return string1 == string1[::-1] or string2 == string2[::-1]

        left = left + 1
        right = right -1

    return True

assert (validPalindrome('aba') == True)
assert (validPalindrome('abca') == True)
assert (validPalindrome('abzxa') == False)

print ('Done!')