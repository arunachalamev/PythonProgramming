# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

# A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

# Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.


def numEnclaves(A):
    m = len(A)
    n = len(A[0])

    def dfs(i,j):
        A[i][j] = 0
        for x,y in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
            if 0<=x<=m-1 and 0<=y<=n-1 and A[x][y]==1:
                dfs(x,y)

    # Flood fill the edge 1's
    for i in range(m):
        for j in range(n):
            if (i==0 or i==m-1 or j==0 or j==n-1) and A[i][j]==1:
                dfs(i,j)

    # return sum of remaining 1's
    return sum(sum(row) for row in A)


print (numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))