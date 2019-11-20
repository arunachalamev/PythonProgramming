# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down, and right. 
# You cannot move through walls. You cannot wrap around the edges of the board.


import collections

def minPathLength ( grid,start, stop):
    pathLength , row, cols  = 0, len(grid), len(grid[0])

    start_i, start_j = start
    stop_i, stop_j = stop

    pathList = collections.deque([[start_i, start_j, pathLength]])

    while len(pathList) > 0:
        cur_i, cur_j, cur_len = pathList.popleft()
        for i,j in {(0,1),(0,-1),(1,0),(-1,0)}:
            next_i, next_j  = cur_i + i,  cur_j + j
            if 0 <= next_i <row and 0<=next_j < cols and grid[next_i][next_j] != 1:
                next_len = cur_len + 1
                pathList.append([next_i,next_j,next_len])
                if next_i == stop_i and next_j == stop_j:
                    return next_len
    
    return -1


start = (3,0)
stop  = (0,0)
print (minPathLength([[0,0,0,0],[1,1,0,1],[0,0,0,0],[0,0,0,0]], start, stop))