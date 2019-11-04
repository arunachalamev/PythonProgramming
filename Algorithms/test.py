import collections

def numberOfWaysToDecode(s):
    if len(s)==0: return 0
    if len(s)==1 and int(s)!=0 : return 1

    dp = [0]*(len(s)+1)
    dp[0]=1

    for i in range(1,len(s)+1):
        if int(s[i-1])!=0:
            dp[i] = dp[i] + dp[i-1]
        if i!=1 and int(s[i-2:i])>=10 and int(s[i-2:i])<=26:
            dp[i] = dp[i] + dp[i-2]
    print (dp)
    return dp[-1]


print(numberOfWaysToDecode('2263'))
print(numberOfWaysToDecode('11'))
