# Given a 2D grid consists of 0s (land) and 1s (water). 
# An island is a maximal 4-directionally connected group of 0s and 
# a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

def closedIslands(grid):
    m = len(grid)
    n = len(grid[0])

    def dfs(i,j):
        grid[i][j] = 1
        for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=x<=m-1 and 0<=y<=n-1 and grid[x][y]==0:
                dfs(x,y)

    #Flood fill 0's available in the edges
    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m-1 or j==0 or j == n-1 ) and grid[i][j]==0:
                dfs(i,j)
    
    #Flood fill 0's and keep counter for islands
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                dfs(i,j)
                count = count + 1
    
    return count


print(closedIslands([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))

