

def canAttendMeetings(intervals):
    intervals = sorted(intervals)
    print (intervals)
    prevE = 0
    for x,y in intervals:
        if prevE < x:
            prevE = y
            continue
        else:
            return False

    return True

print(canAttendMeetings([[0,30],[5,10],[15,20]]))
print (canAttendMeetings([[7,10],[2,4]]))
print (canAttendMeetings([[5,8],[6,8]]))
