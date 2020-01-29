


def shortestPathBinaryMatrix(grid):
    if grid[0][0] or grid[-1][-1]:
        return -1
    n = len(grid)
    q = [(0,0,1)]
    for i,j,d in q:
        if i == n-1 and j == n-1:
            return d
        for x,y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
            if 0<=x<n and 0<=y<n and not grid[x][y]:
                grid[x][y] = 1
                q.append((x,y,d+1))
    return -1

print (shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))