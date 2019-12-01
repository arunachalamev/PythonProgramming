# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.


def countSquares(matrix):
    R,C = len(matrix), len(matrix[0])

    dp = [[0]*(C+1) for _ in range(R+1)]
    ans = 0

    for i,row in enumerate(matrix):
        for j, col in enumerate(row):
            if col:
                dp[i+1][j+1] = min (dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                ans += dp[i+1][j+1]

            # print (i+1,j+1,dp)
    
    return ans

matrix = [[0,1,1,1],
          [1,1,1,1],
          [0,1,1,1]
         ]

print (countSquares(matrix)) #5