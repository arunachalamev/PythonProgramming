
def islandPerimeter(grid):

    def edges(x):
        if not x: return 0
        count =0
        for row in x:
            temp = [0] + row + [0]
            for i in range(len(temp)-1):
                if temp[i] != temp[i+1]:
                    count = count + 1

        return count

    Tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for index, value in enumerate(row):
            Tgrid[index].append(value)
    
    print (Tgrid)

    return edges(grid) + edges(Tgrid)


grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

print(islandPerimeter(grid))