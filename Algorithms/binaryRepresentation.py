def dp(n):
    if n==1:return ['0', '1']
    a = dp(n-1)
    return ['0'+_ for _ in a]+['1'+_ for _ in a[::-1]]

print (dp(4))