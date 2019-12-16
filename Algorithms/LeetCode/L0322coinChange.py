

def coinChange(coins,amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin,amount+1):
            dp[x] = min (dp[x], dp[x-coin]+1)
    return dp[-1] if dp [-1] != float('inf') else -1

print (coinChange([1, 2, 5],11))
print (coinChange([2],3))

