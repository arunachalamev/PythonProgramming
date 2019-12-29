

def minPathSum(grid):

    dp = [ [0]*len(grid[0]) for _ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i ==0 and j == 0:
                dp[i][j] = grid[i][j]
                continue
            if i ==0 :
                dp[i][j] = dp[i][j-1] + grid[i][j]
                continue
            if j ==0 :
                dp[i][j] = dp[i-1][j] + grid[i][j]
                continue
            dp[i][j] = grid[i][j] + min (dp[i][j-1],dp[i-1][j])
    
    return dp[-1][-1]

print (minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))