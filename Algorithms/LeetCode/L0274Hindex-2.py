

def hIndex(citations):
    n = len(citations)
    left, right = 0, n- 1
    while (left <= right):
        pivot = left + (right - left)//2
        if citations[pivot] == n - pivot:
            return n - pivot
        elif citations[pivot] < n- pivot:
            left = pivot + 1
        else:
            right = pivot -1
    
    return n- left

print (hIndex([0,1,3,5,6]))