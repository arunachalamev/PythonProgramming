def getNoZeroIntegers(n):
    for i in range(1,n):
        if '0' in list(str(i)):
            continue
        result = n - i
        if '0' in list(str(result)):
            continue
        return [i,result]

    return None


print (getNoZeroIntegers(2)) #[1,1]
print (getNoZeroIntegers(1010)) #[11,999]
