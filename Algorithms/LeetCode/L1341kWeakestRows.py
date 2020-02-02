


def kWeakestRows(mat, k):
    result = []
    for index, row in enumerate(mat):
        sumcol = 0
        for col in row:
            sumcol += col
        result.append([index,sumcol])
    result.sort(key= lambda v: v[1])
    output = []
    for x,y in result[:k]:
        output.append(x)
    return output

print (kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))


#Output: [2,0,3]
