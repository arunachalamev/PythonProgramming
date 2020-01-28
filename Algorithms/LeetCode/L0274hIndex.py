

def hIndex(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:
            return n-i

    return

print (hIndex([3,0,6,1,5]))