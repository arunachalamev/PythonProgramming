# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.


def countVowelPermutation(n):
    
    dp = list()
    # row are length, column are vowel - 'a','e','i','o','u'
    dp.append([1,1,1,1,1])
    for i in range(1, n):
        dp.append([dp[i-1][1]+dp[i-1][2]+dp[i-1][-1], dp[i-1][0]+dp[i-1][2], dp[i-1][1]+dp[i-1][-2], dp[i-1][2], dp[i - 1][2]+dp[i-1][-2]])
    return sum(dp[-1])%1000000007


print(countVowelPermutation(1))
#All possible strings are: "a", "e", "i" , "o" and "u".


print(countVowelPermutation(2))
#All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua"

