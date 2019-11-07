# Given a positive integer n and you can do operations as follow:
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?

def integerReplacement(n):
    if n == 1: return 0

    if n%2 == 0:
        return 1+ integerReplacement(n/2)
    else:
        return 1+ min(integerReplacement(n-1),integerReplacement(n+1))


#There is a O(log N) algorithm exist based on the properties divisible by 4

print (integerReplacement(8))