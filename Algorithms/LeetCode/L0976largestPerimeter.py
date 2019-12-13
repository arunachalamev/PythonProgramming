
# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

# If it is impossible to form any triangle of non-zero area, return 0.


def largestPerimeter(A):
    A.sort() #increasing order
    for i in range(len(A)-3,-1,-1):
        if A[i+2] < A[i+1] + A[i]:
            return A[i+2]+A[i+1]+A[i]
    return 0

print (largestPerimeter([3,6,2,3]))