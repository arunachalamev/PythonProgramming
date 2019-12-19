

def spiralMatrixIII(R,C, r0, c0):

    result = [(r0,c0)]
    if R*C == 1: return result

    k =1

    while (1):
        for dx,dy,dk in [(0,1,k), (1,0,k), (0,-1,k+1), (-1,0,k+1)]:

            for _ in range(dk):
                r0 += dx
                c0 += dy

                if 0<=r0<R and 0<=c0<C:
                    result.append((r0,c0))
                    if len(result) == R*C:
                        return result
        k += 2


print (spiralMatrixIII(1,4,0,0))
print (spiralMatrixIII(5,6,1,4))

