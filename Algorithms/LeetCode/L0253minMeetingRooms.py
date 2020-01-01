import heapq


def minMeetingRooms(interval):
    interval = sorted(interval, key= lambda x: x[0])
    if len(interval) == 0: return 0
    if len(interval) == 1: return 1
    H = [interval[0][1]]
    heapq.heapify(H)
    for i in interval[1:]:
        if H[0] < i[0]:
            heapq.heappop(H)
        heapq.heappush(H,i[1])
    return len(H)




print (minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print (minMeetingRooms([[7,10],[2,4]]))

