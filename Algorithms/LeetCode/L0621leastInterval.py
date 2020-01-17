
from collections import Counter
from heapq import heappush,heappop

def leastInterval(tasks, n):

    task_count = Counter(tasks)
    current_time = 0
    current_heap = []

    for k,v in task_count.items():
        heappush(current_heap, (-v, k))

    while current_heap:
        index, temp = 0, []
        while index <=n:
            current_time +=1
            if current_heap:
                timing, taksid = heappop(current_heap)
                if timing != -1:
                    temp.append((timing+1,taksid))

            index += 1 
            if not current_heap and not temp:
                break
        for item in temp:
            heappush(current_heap,item)

    return current_time

print (leastInterval(['A','A','A','B','C','D','E'],2 ))
print (leastInterval(['A','A','A','B','B','B'],2 ))

