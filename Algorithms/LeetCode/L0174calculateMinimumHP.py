

def calculateMinimumHP(dungeon):
    R,C = len(dungeon), len(dungeon[0])
    dp = [[float('inf') for _ in range(C+1)] for _ in range(R+1)]

    dp[R][C-1] = 0
    dp[R-1][C] = 0

    for i in range(R-1,-1,-1):
        for j in range(C-1,-1,-1):
            dp[i][j] = max( min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j],0)

    return dp[0][0]+1

print (calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))