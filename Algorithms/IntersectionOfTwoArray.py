
def intersectionOfTwoArray(x,y):

    if len(x) > len(y):
        x,y = y, x

    x.sort()
    y.sort()
    
    i,j = 0,0
    result = []

    while (i<len(x) and j < len(y)):
        if x[i] == y[j]:
            result.append(x[i])
            i = i +1
            j = j +1
        elif x[i] < y[j] :
            i = i + 1
        elif x[i] > y[j]:
            j = j + 1

    print (result)

    return  result

intersectionOfTwoArray([1,2,3,3,4],[1,2,3,3,5,6,7,9])

