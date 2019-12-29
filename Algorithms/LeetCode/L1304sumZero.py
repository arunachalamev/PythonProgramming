

def sumZero(n):
    if n==1: return [0]
    result = []

    value = n//2
    for x in range(-value,value+1):
        result.append(x)

    if n%2 ==0:
        result.remove(0)

    return result

