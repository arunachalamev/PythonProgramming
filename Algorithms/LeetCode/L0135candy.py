import collections

def candy(ratings):
    graph = [[] for x in range(len(ratings))]
    for i in range(len(ratings)-1):
        if ratings[i] < ratings[i+1]:
            graph[i].append(i+1)
        elif ratings[i] > ratings[i+1]:
            graph[i+1].append(i)

    print (graph)

    loser = [True]*len(ratings)
    for u,row in enumerate(graph):
        for v in row:
            loser[v] = False

    print (loser)

    queue = collections.deque((node,1) for node,v in enumerate(loser) if v)
    ans = [0]*len(ratings)
    while queue:
        node, d = queue.popleft()
        ans[node] = d
        for nei in graph[node]:
            queue.append((nei, d+1))

    print (ans)
    return ans

def candy2 (ratings):
    ans = [1]* len(ratings)
    N =len(ratings)
    for i in range(N-1):
        if ratings[i] < ratings[i+1]:
            ans[i+1] = ans[i] + 1

    for i in range(N-1,-1,-1):
        if ratings[i] > ratings[i+1]:
            ans[i] = max (ans[i], ans[i+1]+1)
    return sum(ans)

# print(candy([1,0,2]))
# print(candy([1,2,2]))

print(candy2([1,0,2]))
print(candy2([1,2,2]))
