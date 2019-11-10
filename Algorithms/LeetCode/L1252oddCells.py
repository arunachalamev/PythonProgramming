def oddCells(n,m,indices):

    mat = [[0]*m for _ in range(n)]

    print ((mat))

    for i,j in indices:
        for col in range(m):
            mat[i][col] += mat[i][col]
        for row in range(n):
            mat[row][j] += mat[row][j]
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] %2 == 1:
                result = result + 1

    return None

oddCells(2,3,[[0,1],[1,1]])


