# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, 
# where in each step you can delete one character in either string.

# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

def minDistance(word1, word2):
    m,n = len(word1), len(word2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = max (dp[i+1][j], dp[i][j+1], dp[i][j]+ (word1[i]==word2[j]))
    
    return m+n - 2*dp[m][n]


print (minDistance('sea','eat'))