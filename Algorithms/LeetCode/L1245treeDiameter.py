# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

import collections

def treeDiameter (edges):
    if len(edges) == 0: return 0
    numOfNodes = len(edges) + 1
    graph = [[] for _ in range(numOfNodes)]

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(source):
        queue = collections.deque([[source,0]])
        seen = {source}
        while queue:
            node, d = queue.popleft()
            neighbours = graph[node]
            for nei in neighbours:
                if nei not in seen:
                    seen.add(nei)
                    queue.append([nei,d+1])
        return node,d

    far, d = bfs(0)
    far2,d = bfs(far)

    return d

print (treeDiameter([[0,1],[0,2]]))
print (treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))
