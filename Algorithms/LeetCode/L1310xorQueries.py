

def xorQueries(arr,queries):
    P = [0]
    for x in range(0,len(arr)):
        P.append(P[-1] ^ arr[x])

    print (arr, P)
    result = []
    for x,y in queries:
        result.append (P[y+1] ^ P[x])

    return result

print (xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))
