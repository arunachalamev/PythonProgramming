# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

def isToeplitzMatrix(matrix):
    m,n = len(matrix), len(matrix[0])

    flag = [[False]*n for _ in range(m)]

    for i in range(n):
        flag[0][i] = True
    for i in range(m):
        flag[i][0] = True

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == matrix[i-1][j-1]:
                flag[i][j] = flag[i-1][j-1]
            else:
                return False
    
    return True

print (isToeplitzMatrix([[1,2],[2,2]]))
print (isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))
#Sol1
def isToeplitzMatrix1(matrix):
    groups = {}
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r-c not in groups:
                groups[r-c] = val
            elif groups[r-c] != val:
                return False
    return True

#Sol2
def isToeplitzMatrix2(matrix):
    return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                for r, row in enumerate(matrix)
                for c, val in enumerate(row))


