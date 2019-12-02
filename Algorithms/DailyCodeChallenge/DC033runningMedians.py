import heapq as hq
def runningMedians(arr):

    minHeap, maxHeap, median = list(), list(), list()

    for x in arr:
        hq.heappush(minHeap,x)
        if len(minHeap) > len(maxHeap) + 1:
            smallestElementFromMinHeap = hq.heappop(minHeap)
            hq.heappush(maxHeap, -smallestElementFromMinHeap )
        
        if len(minHeap) == len(maxHeap):
            median.append((minHeap[0] - maxHeap[0])/2.0)
        else:
            median.append(minHeap[0])
    return median

print(runningMedians([2,5]))
print(runningMedians([3,3,3,3,3]))
print(runningMedians([2, 1, 5, 7, 2, 0, 5]))
