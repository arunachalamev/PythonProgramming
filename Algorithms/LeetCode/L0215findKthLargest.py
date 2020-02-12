import heapq

def findKthLargest(nums, k):
    temp = []
    for x in nums:
        temp.append(-x)
    heapq.heapify(temp)
    for _ in range(k-1):
        heapq.heappop(temp)
    
    return -1*temp[0]

print (findKthLargest([3,2,1,5,6,4],2))