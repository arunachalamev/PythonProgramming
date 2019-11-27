# Given an array that stores a complete Binary Search Tree, write a function that efficiently prints the given array in ascending order.
# For example, given an array [4, 2, 5, 1, 3], the function should print 1, 2, 3, 4, 5

def completeBinaryTreeInArrayToSortedOrder(A,start,end):

    if start>end:
        return
    
    completeBinaryTreeInArrayToSortedOrder(A,2*start+1,end)
    print (A[start])
    completeBinaryTreeInArrayToSortedOrder(A,2*start+2,end)

    return


print (completeBinaryTreeInArrayToSortedOrder([4,2,5,1,3],0,4))