

def minFallingPathSum(A):
    pathSum = [[float('inf')]*len(A[0]) for _ in range(len(A))]
    i,j  = 0, 0
    while j<len(A[0]):
        pathSum[i][j] = A[i][j]
        j +=1

    for i in range(1,len(A)):
        for j in range(len(A[i])):
            for k in (j-1, j, j+1):
                if 0<=k<len(A[0]):
                    pathSum[i][j] = min(pathSum[i][j], pathSum[i-1][k]+ A[i][j])
                    # pass

    # print (pathSum)
    return min (pathSum[-1])

print (minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))