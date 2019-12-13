
# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.


def NumOfWaysCoinChange(amount, coins):

    dp = [0]*(amount+1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin,amount+1):
            dp[x] = dp[x] + dp [x-coin]

    return dp[amount]


print (NumOfWaysCoinChange(5,[1,2,3]))
