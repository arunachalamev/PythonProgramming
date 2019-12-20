

def sortArrayByParity(a):
    i, j = 0, len(a)-1

    while i<j:
        if a[i]%2 == 1 and a[j]%2 == 0:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        
        if a[i]%2 == 0:
            i +=1
        
        if a[j]%2 == 1:
            j -=1

    return a
        
print (sortArrayByParity([3,1,2,4]))