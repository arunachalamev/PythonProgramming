

def addToArrayForm(A,K):
    temp =''
    for x in A:
        temp = temp + str(x)

    result = []
    for x in str(int(temp)+K):
        result.append(x)

    return result


print(addToArrayForm([1,2,0,0],34))