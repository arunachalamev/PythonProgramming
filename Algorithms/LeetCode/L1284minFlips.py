
import itertools

def minFlips(A):
    R, C = len(A), len(A[0])
    N = R*C
    ans = N + 1
    for cand in itertools.product(range(2), repeat = N):
        bns = sum(cand)
        # if bns >= ans: continue
        r=c= 0
        B = [row[:] for row in A]
        for adj in cand:
            if adj:
                B[r][c] ^= 1
                for nr, nc in ((r-1,c), (r, c-1), (r, c+1), (r+1, c)):
                    if 0 <= nr < R and 0 <= nc < C:
                        B[nr][nc] ^= 1
            c += 1
            if c == C:
                c = 0
                r += 1
        
        if sum(sum(row) for row in B) == 0:
            ans = bns
    return ans if ans < N+1 else -1


print(minFlips([[0,0],[0,1]]))
print(minFlips([[0]]))
print (minFlips([[1,1,1],[1,0,1],[0,0,0]]))
print (minFlips([[1,0,0],[1,0,0]]))