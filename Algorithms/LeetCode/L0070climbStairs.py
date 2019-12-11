
def climbStairs(n):
    dp = []
    dp.append(1)
    dp.append(2)

    for _ in range(3,n+1):
        dp.append(dp[-1]+dp[-2])

    return dp[-1]

print(climbStairs(2))
print(climbStairs(3))
