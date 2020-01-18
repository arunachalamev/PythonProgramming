

def merge(intervals):
    intervals.sort(key= lambda x: x[0])
    result = [intervals[0]]
    for x in intervals[1:]:
        if x[0] <= result[-1][1]:
            result[-1][1] = max(x[1],result[-1][1])
        else:
            result.append(x)
    return result

print (merge([[1,3],[2,6],[15,18],[8,10]]))
print (merge([[1,4],[4,5]]))
