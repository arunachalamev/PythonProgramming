

def findTheCity(n,edges,dist_threshold):
    dist = [[float('inf')]*n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0

    for x,y,z in edges:
        dist[x][y] = dist[y][x] = z

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min (dist[i][j], dist[i][k]+ dist[k][j])

    best_reached = float('inf')
    for u in range(n):
        reached = sum (dist[u][v] <= dist_threshold for v in range(n))
        if reached <= best_reached:
            ans = u
            best_reached = reached
    return ans


print (findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))