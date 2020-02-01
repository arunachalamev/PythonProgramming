


def generateMatrix(n):
    A = [[0]*n for _ in range(n)]
    i,j = 0,0
    di, dj = 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n] :
            di, dj = dj, -di
        i = i + di
        j = j + dj

    return A

print (generateMatrix(4))