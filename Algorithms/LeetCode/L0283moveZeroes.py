

def moveZeroes(a):
    i, j = 0, 1
    while a[i] !=0:
        i +=1
    j = i+1
    while (j<len(a)):
        if a[j] != 0:
            a[i] = a[j]
            a[j] = 0
            i +=1
            j +=1
        else:
            j +=1

    return None


l = [1,0,0,3,12]
moveZeroes(l)
print (l)