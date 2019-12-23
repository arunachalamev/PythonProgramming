


def numMovesStones(a,b,c):
    minX = min(a,b,c)
    maxX = max(a,b,c)

    a,b,c = sorted([a,b,c])
    if a+1 == b or b+1== c:
        minimum = 1
    elif a+2==b or b+2 == c:
        minimum = 1
    else:
        minimum = 2
    
    maximum = maxX-minX-2
    if maximum == 0:
        minimum = 0
    return (minimum,maximum)


print(numMovesStones(1,2,5))
print(numMovesStones(4,3,2))
print(numMovesStones(3,5,1))

