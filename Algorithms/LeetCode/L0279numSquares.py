

def numSquares(n):

    squares = [i*i for i in range(n) if i*i <= n]
    print (squares)
    dp = [i for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for s in squares:
        for i in range(s,n+1):
            dp[i] = min(dp[i], dp[i-s]+1)
    print (dp)
    return dp[-1]

print (numSquares(4))