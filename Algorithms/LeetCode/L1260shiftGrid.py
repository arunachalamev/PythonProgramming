
def shiftGrid(grid, k):
    result,temp = [], []
    rows, cols = len(grid), len(grid[0])
    if k>rows*cols : k = k%(rows*cols)

    for i in grid:
        for j in i:
            temp.append(j)

    left, right = temp [-k:], temp [:-k]

    temp = left + right 


    for i in range(0,len(temp),cols):
        result.append(list(temp[i:i+cols]))

    return result

print (shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1))