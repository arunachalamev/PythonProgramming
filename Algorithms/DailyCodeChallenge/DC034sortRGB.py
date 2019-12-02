# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first, 
# the Gs come second, and the Bs come last. You can only swap elements of the array.

def sortRGB(A):
    i,j,k = 0,0,len(A)-1

    while (j<=k):
        if A[j] == 'R':
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j + 1
        elif A[j] == 'B':
            A[j], A[k] = A[k], A[j]
            k = k -1
        else:
            j = j + 1

    return A


#if Number 0,1,2 is given
def sortRGB2(A):
    i,j,k = 0,0,len(A)-1

    while (j<=k):
        if A[j] < 1:
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j + 1
        elif A[j] > 1:
            A[j], A[k] = A[k], A[j]
            k = k -1
        else:
            j = j + 1

    return A


print (sortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print (sortRGB2([1,1,1,2,2,2,0,0,0]))
