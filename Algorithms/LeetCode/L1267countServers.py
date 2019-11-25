# You are given a map of a server center, represented as a m * n integer matrix grid, 
# where 1 means that on that cell there is a server and 0 means that it is no server. 
# Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

def countServer(grid):
    if not grid: return 0

    rows = len(grid)
    cols = len(grid[0])

    row = [0]* rows
    col = [0]* cols
    for i in range(rows):
        row[i] = sum(grid[i])

    transpose = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))] 

    for i in range(len(transpose)):
        col[i] = sum(transpose[i])

    # print (row,col)

    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if row[i] > 1 or col[j] > 1:
                    count = count + 1


    return count


print (countServer([[1,0],[0,1]]))
print (countServer([[1,0],[1,1]]))

print (countServer([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
