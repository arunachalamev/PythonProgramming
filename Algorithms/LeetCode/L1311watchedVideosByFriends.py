
import collections

def wathcedVideosByFriends(watchedVideos,friends,uid,level):
    seen = {uid}
    queue = collections.deque([(uid,0)])

    friendsAtDepth = set()
    while queue:
        node, d = queue.popleft()
        if d > level: break
        if d == level: friendsAtDepth.add(node) 

        for nei in friends[node]:
            if nei not in seen:
                seen.add(nei)
                queue.append((nei,d+1))
    
    count = collections.Counter()
    for f in friendsAtDepth:
        for video in watchedVideos[f]:
            count[video] +=1
    
    result = sorted( count.keys(), key=lambda x: (count[x],x))
    return result

print (wathcedVideosByFriends([["A","B"],["C"],["B","C"],["D"]],[[1,2],[0,3],[0,3],[1,2]],0,1))