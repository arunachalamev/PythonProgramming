

def partitionSum(A):
    sumX = sum(A)
    if sumX%2 == 1: return False
    else: traget = sumX//2

    possibleSum = set(A)
    for x in A:
        Temp = list()
        for z in possibleSum:
            Temp.append(z+x)
            if traget in possibleSum:
                return True
        possibleSum.update(set(Temp))

    return False

print (partitionSum([1,2,3]))
print (partitionSum([15,5,20,10,35,15,10]))
print (partitionSum([15,5,20,10,35]))

