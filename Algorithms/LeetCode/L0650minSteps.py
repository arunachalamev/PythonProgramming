

# def minSteps(n):
#     s = 0
#     for d in range(2,n+1):
#         while (n%d == 0):
#             print (d,s)
#             s += d
#             n /= d
#             print ("....",d,s)
#     return s

def minSteps(n):
    dp = [0]*(n+1)
    for i in range(2, n+1):
        dp[i] = i
        for j in range(i-1,0,-1):
            if (i%j == 0):
                dp[i] = dp[j] + (i//j)
                break
    print (dp)
    return dp[-1]


print (minSteps(10))