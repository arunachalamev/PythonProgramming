import collections

def minJumps(arr):
    index = collections.defaultdict(list)
    _ = [ index[v].append(i) for i,v in enumerate(arr)]

    print (index)

    queue = collections.deque([(0,0)])
    # queue.append((0,0))
    num_met, pos_met = set(), set ()
    while queue:
        pos, step = queue.popleft()
        if pos == len(arr)-1: return step
        num = arr[pos]
        pos_met.add(pos)
        for p in [pos-1,pos+1] + index[num]* (num not in num_met):
            if p in pos_met or  not 0 <=p<len(arr): continue
            queue.append((p,step+1))
        num_met.add(num)

    return

print (minJumps([100,-23,-23,404,100,23,23,23,3,404]))