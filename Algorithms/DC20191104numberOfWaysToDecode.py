
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


def numberOfWaysToDecode(str):

    dp = [0]* (len(str) + 1)
    dp[0] = 1

    for i in range (1, len(str)+1):
        if int(str[i-1]) !=0:
            dp[i] = dp[i] + dp[i-1]
        if i!=1 and int(str[i-2:i]) <= 26 and int(str[i-2:i]) >= 10:
            dp[i] = dp[i] + dp[i-2]
    
    print (dp)
    return (dp[len(str)])


print(numberOfWaysToDecode('2263'))
print(numberOfWaysToDecode('111'))
