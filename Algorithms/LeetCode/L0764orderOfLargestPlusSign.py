


def orderOfLargestPlusSign(N,mines):
    r,c = 0, N-1
    banned = {tuple(mine) for mine in mines}
    ans = 0
    for r in range(N):
        for c in range(N):
            k= 0
            while ( k<=r<N-k and k<=c<N-k and
                (r-k,c) not in banned and
                (r,c-k) not in banned and
                (r,c+k) not in banned and
                (r+k,c) not in banned):
                    k += 1
            ans = max(ans,k)
    return ans


def orderOfLargestPlusSignDP(N,mines):
    ans = 0
    dp = [[0]*N for _ in range(N)]
    banned = {tuple(mine) for mine in mines}
    for r in range(N):
        count = 0
        for c in range(N):
            count = 0 if (r,c) in banned else count + 1
            dp[r][c] = count

        count = 0
        for c in range(N-1,-1,-1):
            count = 0 if (r,c) in banned else count + 1
            if count < dp[r][c]: dp[r][c] = count

    
    for c in range(N):
        count = 0
        for r in range(N):
            count = 0 if (r,c) in banned else count + 1
            if count < dp[r][c]: dp[r][c] = count

        count = 0
        for r in range(N-1,-1,-1):
            count = 0 if (r,c) in banned else count + 1
            if count < dp[r][c]: dp[r][c] = count

            if ans < dp[r][c]: ans = dp[r][c]

    return ans

print (orderOfLargestPlusSign(5,[[4,2]]))
print (orderOfLargestPlusSignDP(5,[[4,2]]))
