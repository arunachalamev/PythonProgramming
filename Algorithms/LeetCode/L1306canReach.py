import collections

def canReach(arr, start):
    dq = collections.deque()

    dq.append(start)
    plusvisited = set()
    minusvisited = set()
    while dq:
        i = dq.popleft()
        if 0<= i+arr[i] < len(arr) and not i+arr[i] in plusvisited:
            dq.append(i+arr[i])
            plusvisited.add(i+arr[i])
            if arr[i+arr[i]] == 0: return True
        if 0<= i-arr[i] < len(arr) and not i-arr[i] in minusvisited:
            dq.append(i-arr[i])
            minusvisited.add(i-arr[i])
            if arr[i-arr[i]] == 0: return True

    return False

