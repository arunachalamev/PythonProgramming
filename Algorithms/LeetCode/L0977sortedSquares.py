

def sortedSquares(A):
    i,j = 0, len(A)-1
    if A is None: return []
    result = list()
    while (i<=j):
        if A[i]**2 <= A[j]**2:
            result.append (A[j]**2)
            j = j - 1
        else:
            result.append (A[i]**2)
            i = i +1
    return result[::-1]

print (sortedSquares([-4,-1,0,3,10]))

print (sortedSquares([-7,-3,2,3,11]))