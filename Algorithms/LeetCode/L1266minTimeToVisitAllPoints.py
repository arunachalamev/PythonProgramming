# On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
# Your task is to find the minimum time in seconds to visit all points.

# You can move according to the next rules:

# In one second always you can either move vertically, horizontally by one unit or diagonally 
# (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

def minTimeToVisitAllPoints(points):
    if len(points) ==0: return 0

    result = 0
    first = 1

    for x,y in points:
        if first:
            prev_x, prev_y = x,y
            first = 0
        else:
            result = result + max(abs(x-prev_x),abs(y-prev_y))
            prev_x, prev_y = x, y

    return result

print (minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print (minTimeToVisitAllPoints([[3,2],[-2,2]]))