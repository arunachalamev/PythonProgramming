# A group of two or more people wants to meet and minimize the total travel distance.
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# Find the total distance that needs to be travelled to reach this meeting point.

def bestMeetingPoint(grid):

    if len(grid)==0: return 0

    row, col = list(), list()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                row.append(i)
                col.append(j)
    
    row.sort()
    col.sort()
    result = 0

    midX, midY = row[len(row)//2], col[len(col)//2]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                result = result + abs(i-midX) + abs(j-midY)

    return result


grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0],[0, 0, 1, 0, 0]]


print (bestMeetingPoint(grid))