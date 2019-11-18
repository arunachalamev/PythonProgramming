# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
# find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def minClassRoom(inputList):

    startTime = dict ()
    endTime   = dict ()

    if len(inputList) == 0: return 0

    for s,e in inputList:
        if s not in startTime:
            startTime[s] = 0
        startTime[s] += 1

        if e not in endTime:
            endTime[e] = 0
        endTime[e] += 1

    minTime = min(startTime)
    maxTime = max(endTime)

    currentClassRoomCount = 0
    maxCount = 0

    for i in range (minTime, maxTime):
        if i in startTime:
            currentClassRoomCount += startTime[i]

        if currentClassRoomCount> maxCount:
            maxCount = currentClassRoomCount

        if i in endTime:
            currentClassRoomCount -= endTime[i]

    return maxCount

assert minClassRoom([]) == 0
assert minClassRoom([(30, 75), (0, 50), (60, 150)]) == 2
assert minClassRoom([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert minClassRoom([(60, 150)]) == 1
assert minClassRoom([(60, 150), (150, 170)]) == 2
assert minClassRoom([(60, 150), (60, 150), (150, 170)]) == 3

print ('Done!')