
import collections
def diagonalSort(mat):
    coll = collections.defaultdict(list)
    for r,row in enumerate(mat):
        for c, value in enumerate(mat[r]):
            coll[r-c].append(value)
    print (coll)

    for val in coll.values():
        val.sort(reverse=True)

    for r,row in enumerate(mat):
        for c, value in enumerate(mat[r]):
            mat[r][c]= coll[r-c].pop()
    return mat

print (diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))