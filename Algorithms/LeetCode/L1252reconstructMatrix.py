# Given the following details of a matrix with n columns and 2 rows :
# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], 
# where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.
# Return it as a 2-D integer array.
# If there are more than one valid solution, any of them will be accepted.
# If no valid solution exists, return an empty 2-D array.


def reconstructMatrix(upper,lower,colsum):
    if upper+lower != sum(colsum):
        return []

    a = [[0]*len(colsum) for _ in {0,1}]
    delta = 0

    for i,c in enumerate(colsum):
        if c == 2:
            a[0][i] = a[1][i] = 1
        elif c == 1:
            delta = delta + 1

    upperRow = sum(a[0])
    lowerRow = sum(a[1])

    remainingUpperRow = upper - upperRow
    remainingLowerRow = lower - lowerRow

    if delta != remainingLowerRow + remainingUpperRow : return []
    if remainingUpperRow <0 or remainingLowerRow <0: return []

    for i,c in enumerate(colsum):
        if c == 1:
            if remainingUpperRow:
                remainingUpperRow = remainingUpperRow - 1
                a[0][i] =1
            else:
                remainingLowerRow = remainingLowerRow - 1
                a[1][i] = 1
        
    return a


print (reconstructMatrix(2,1,[1,1,1]))