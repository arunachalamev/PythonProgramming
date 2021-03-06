

def minCostClimbingStairs(cost):
    dp = [float('inf')]*len(cost)
    # cost[-1] =0
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
    
    return min(dp[-2],dp[-1])

print (minCostClimbingStairs([10,15,20]))
print (minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

