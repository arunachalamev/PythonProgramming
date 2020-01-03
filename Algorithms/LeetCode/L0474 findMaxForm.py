

def findMaxForm(strs,m,n):
    dp = [ [0]*(n+1) for _ in range(m+1)]

    def count(s):
        return sum(1 for c in s if c=='0'), sum(1 for c in s if c=='1')
    
    for z,o in [count(s) for s in strs]:
        for x in range(m,-1,-1):
            for y in range(n,-1,-1):
                if x>=z and y>=o:
                    dp[x][y] = max(1+dp[x-z][y-o], dp[x][y])
        print (dp)
    
    return dp[-1][-1]


print (findMaxForm(["10", "0001", "111001", "1", "0"],5,3))
