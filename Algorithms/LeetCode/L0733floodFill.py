

def floodFill(image,sr,sc,newColor):
    R,C = len(image), len(image[0])
    if sr> R or sc >C: return imgage
    TrackPos = [(sr,sc)]

    currentPixel = image[sr][sc]
    if currentPixel == newColor: return image
    while TrackPos:
        i,j = TrackPos.pop()
        for x,y in [(i,j), (i,j+1), (i,j-1), (i+1,j), (i-1,j)]:
            if 0<=x<R and 0<=y<C:
                if image[x][y] == currentPixel:
                    TrackPos.append((x,y))
                    image[x][y] = newColor

    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
