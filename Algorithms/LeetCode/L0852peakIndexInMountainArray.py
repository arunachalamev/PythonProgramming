

def peakIndexInMountainArray(A):

    for i in range(1,len(A)-1):
        if A[i-1]<A[i]>A[i+1]:
            return i
        
    return None

print(peakIndexInMountainArray([0,2,1,0]))

