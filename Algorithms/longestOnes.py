def longestOnes(A,K):
    left, right = 0, 0
    max_len = 0

    while (right < len(A)):
        K = K - (1 - A[right])

        if K<0:
            K = K + (1 - A[left])
            left = left + 1
        
        right = right + 1

        if max_len < (right-left):
            max_len = right - left

    return max_len

print (longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print (longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
