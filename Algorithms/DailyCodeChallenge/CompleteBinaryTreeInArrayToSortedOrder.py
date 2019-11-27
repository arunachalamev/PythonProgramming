
def completeBinaryTreeInArrayToSortedOrder(A,start,end):

    if start>end:
        return
    
    completeBinaryTreeInArrayToSortedOrder(A,2*start+1,end)
    print (A[start])
    completeBinaryTreeInArrayToSortedOrder(A,2*start+2,end)

    return


print (completeBinaryTreeInArrayToSortedOrder([4,2,5,1,3],0,4))