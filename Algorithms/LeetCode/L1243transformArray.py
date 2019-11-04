def transformArray(arr):
    if len(arr) <= 2 : return arr

    prevArray, result  = arr.copy(), arr.copy()
    currentArray = []

    while (prevArray != currentArray) :

        prevArray = result.copy()
        currentArray = prevArray.copy()

        for i in range (1,len(prevArray)-1):
            if prevArray[i-1]>prevArray[i] and prevArray[i+1] > prevArray[i]:
                currentArray[i] = prevArray[i] + 1
            if prevArray[i-1]<prevArray[i] and prevArray[i+1] < prevArray[i]:
                currentArray[i] = prevArray[i] - 1
        result = currentArray.copy()

    return prevArray
 

print (transformArray([6,2,3,4]))
print (transformArray([1,6,3,4,3,5]))
print(transformArray([2,1,2,1,1,2,2,1]))

