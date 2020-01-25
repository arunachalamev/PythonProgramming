

def arrayRankTransform(arr):
    temp = sorted(set(arr))
    # print (arr,temp)
    rank ={}
    i = 1
    for n in temp:
        rank[n] = i
        i = i + 1
    result = []
    for x in arr:
        result.append(rank[x])
    # print (rank)
    return result

print (arrayRankTransform([40,10,20,30]))
print (arrayRankTransform([100,100,100]))
