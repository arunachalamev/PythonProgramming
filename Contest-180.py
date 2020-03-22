
def findTheDistanceValue(arr1, arr2,d):
    count, flag = 0, True
    for i in arr1:
        flag = True
        for j in arr2:
            if abs(i-j)<= d:
                flag = False
                break
        if flag == True:
            count +=1
    return count

# print(findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
# print(findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
# print(findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))


import collections
def maxNumberOfFamilies (n, reservedSeats):
    reservedSeats.sort(key=lambda x: (x[0],x[1]))
    d = collections.defaultdict(list)
    for x,y in reservedSeats:
        d[x].append(y)
    total = 0
    for x in range(1,n+1):
        b2345 = b4567 = b6789 = True
        for y in d[x]:
            if y in [2,3]:
                b2345 = False
            if y in [4,5]:
                b2345 = False
                b4567 = False
            if y in [6,7]:
                b6789 = False
                b4567 = False
            if y in [8,9]:
                b6789 = False
        if b2345 + b4567 + b6789 > 2:
            total += 2
        else:
            total += b2345 or b4567 or b6789
    return total

print (maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
print (maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))
print (maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))


def getKth(lo,hi,k):
    if lo == 1 and hi == 1:
        return 1

    def recurse(n):
        if n == 1:
            return 0
        if n%2 == 0:
            return 1 + recurse(n//2)
        else:
            return 1+ recurse(3*n+1)

    temp = []
    for x in range(lo, hi+1):
        temp.append((x,recurse(x)))
    temp.sort(key=lambda x:(x[1],x[0]))
    return temp[k-1][0]

# print (getKth(lo = 12, hi = 15, k = 2))
# print (getKth(lo = 1, hi = 1, k = 1))
# print (getKth(lo = 7, hi = 11, k = 4))
# print (getKth(lo = 10, hi = 20, k = 5))
# print (getKth(lo = 1, hi = 1000, k = 777))



