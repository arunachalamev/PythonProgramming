# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the 
# set of real numbers x such that a <= x < b.
# We remove the intersections between any interval in intervals and the interval toBeRemoved.
# Return a sorted list of intervals after all such removals.

def removeInterval(intervals, toBeRemoved):

    if len(toBeRemoved) == 0 : return intervals
    start, end = toBeRemoved
    result = []
    for i,j in intervals:
        if start <i < end  and start <j < end:
            continue
        if i< start < j :
            result.append([i,start])
            if end < j: result.append([end,j])
            continue
        if i< end < j :
            result.append([end,j])
            continue
        else:
            result.append([i,j])
    return result



print(removeInterval([[0,2],[3,4],[5,7]],[1,6])) # [[0,1],[6,7]]
print(removeInterval([[0,5]],[2,3])) #[[0,2],[3,5]]
