
def isMonotonic(A):
    i = 1
    increasing, decreasing = 0,0
    while i< len(A):
        if A[i-1] <= A[i]:
            increasing += 1
        if A[i-1] >= A[i]:
            decreasing +=1
        i +=1
    
    if increasing == len(A)-1 or decreasing == len(A) -1 :
        return True
    else:
        return False

print (isMonotonic([1,2,2,3]))
print (isMonotonic([6,5,4,4]))
print (isMonotonic([1,3,2]))
print (isMonotonic([1,2,4,5]))
print (isMonotonic([1,1,1,1]))



