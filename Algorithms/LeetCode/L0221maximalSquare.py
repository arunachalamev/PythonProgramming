

def maximalSquare(matrix):
    maxSquare = float('-inf')
    R,C = len(matrix), len(matrix[0])
    dp = [[0]*(C+1) for _ in range(R+1)]

    for i in range(1,R+1):
        for j in range(1,C+1):
            if matrix[i-1][j-1]:
                dp[i][j] = 1+ min (dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) 
                maxSquare = max(dp[i][j], maxSquare)
    
    return maxSquare*maxSquare

print (maximalSquare([[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]]))