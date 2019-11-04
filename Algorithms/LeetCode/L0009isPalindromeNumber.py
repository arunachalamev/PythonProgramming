# To check whether the given number is palindrome 
# without converting them into string
# O(n)
def isPalindrome(x):
    input = x
    if x < 0:
        return False

    reverseNumber = 0
    while (x>0):
        reverseNumber = reverseNumber * 10 + x %10
        x = x//10
    
    if input == reverseNumber : return True
    else: return False

print(isPalindrome(10))