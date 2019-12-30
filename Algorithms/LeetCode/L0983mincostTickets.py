
def mincostTickets(days,cost):
    dp = [0]* (max(days)+1)
    print (dp)

    for i in range(1,days[-1]+1):
        if i not in days:
            dp[i] = dp[i-1]
        else:
            dp[i] = min (dp[max(0,i-1)]+cost[0], 
                        dp[max(0,i-7)]+cost[1], 
                        dp[max(0,i-30)]+cost[2])
    print (dp)
    return dp[-1]

print (mincostTickets([1,4,6,7,8,20], [2,7,15]))
print (mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
print (mincostTickets([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29],[3,14,50]))

