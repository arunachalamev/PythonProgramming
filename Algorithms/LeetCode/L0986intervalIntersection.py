

def intervalIntersection(A,B):
    i, j = 0, 0

    ans = []
    while i<len(A) and j<len(B):

        lo = max(A[i][0], B[j][0])
        high = min(A[i][1], B[j][1])

        # print (lo,high)
        if lo <= high:
            ans.append([lo,high])

        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    
    return ans

print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))