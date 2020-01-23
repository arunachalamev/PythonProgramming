

def numIslands(grid):
    count = 0

    def DFS(i,j):
        if i< 0 or i > len(grid)-1 or j <0 or j > len(grid[i])-1 or grid[i][j] == 0:
            return 

        grid[i][j] = 0
        DFS(i+1,j)
        DFS(i-1,j)
        DFS(i,j+1)
        DFS(i,j-1)
        return


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count +=1
                DFS(i,j)

    return count


# print (numIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))
print (numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]))
