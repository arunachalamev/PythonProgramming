
def maxSideLength(mat,threshold):
    R,C = len(mat), len(mat[0])
    s = [[0]*(C+1) for _ in range(R+1)]
    for i in range(R):
        for j in range(C):
            s[i+1][j+1] = mat[i][j]+s[i+1][j]+s[i][j+1]-s[i][j]
    # print (s)

    ans=0
    for size in range(min(R,C)+1,0,-1):
        for i in range(R-size+1):
            for j in range(C-size+1):
                p = i + size
                q = j + size
                if s[p][q] - s[i][q] - s[p][j] + s[i][j] <= threshold:
                    return size

    return ans

print(maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],4))
print(maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],1))
print(maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]],6))
print(maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]],40184))


