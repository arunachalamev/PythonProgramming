
import heapq

def minRefuelStops(target, startFuel, stations):
    pq =[]
    stations.append([target,float('inf')])

    tank = startFuel
    ans, prev= 0, 0
    for location,capacity in stations:
        tank = tank -(location - prev)
        while pq and tank<0:
            tank = tank + (-heapq.heappop(pq))
            ans = ans + 1
        if tank < 0: return -1
        heapq.heappush(pq,-capacity)
        prev = location
    
    return ans

print (minRefuelStops(1,1,[]))
print (minRefuelStops(100,1,[[10,100]]))
print (minRefuelStops(100,10,[[10,60],[20,30],[30,30],[60,40]]))
