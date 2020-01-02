
def lastStoneWeightII(stones):
    totalsum = sum(stones)
    dp = [0]* (totalsum+1)
    dp[0] = 1
    for i in range(len(stones)):
        for j in range(totalsum-1,-1,-1):
            if j-stones[i] <0: break
            if dp[j-stones[i]]:
                dp[j] = 1
    
    result = totalsum+1
    for partialsum in range(1,totalsum+1):
        if dp[partialsum] and 2*partialsum-totalsum>=0:
            result = min (result, 2*partialsum-totalsum)
    return result


print (lastStoneWeightII([2,7,4,1,8,1]))
print (lastStoneWeightII([1,2,4,8,16,32,64,12,25,51]))