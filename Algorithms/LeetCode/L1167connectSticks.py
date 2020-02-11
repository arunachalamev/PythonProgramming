import heapq

def connectSticks(A):
    heapq.heapify(A)
    ans = 0

    while (len(A)>1):
        x,y = heapq.heappop(A), heapq.heappop(A)
        ans += x + y
        heapq.heappush(A,x+y)
    return ans


print(connectSticks([2,3,4]))
print(connectSticks([1,8,3,5]))
