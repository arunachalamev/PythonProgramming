

def fib(N):
    a, b = 0, 1
    if N == 0: return 0
    if N == 1 : return 1
    sum = 0

    for i in range(2,N+1):
        sum = a + b
        a = b
        b = sum
    
    return sum

print(fib(4))