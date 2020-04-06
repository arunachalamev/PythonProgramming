import collections
def countLargestGroup(n):
    d = collections.defaultdict(list)
    for i in range (1,n+1):
        str_i = str(i)
        temp = sum([int(x) for x in str_i ])
        # print (str_i,temp)
        d[temp].append(i)
    # print (d)
    l  = []
    for _,v in d.items():
        l.append(len(v))
        # print (k,v)
    count  = collections.Counter(l)
    # print (count)
    res =  (sorted(count.items() , key = lambda p: p[0], reverse= True))
    return res[0][1]

# print (countLargestGroup(13))
# print (countLargestGroup(2))
# print (countLargestGroup(15))
# print (countLargestGroup(24))


def canConstruct(s,k):

    def isallowed(x, L):
        if x%2 ==0: return True
        elif sum([e%2 for e in L]) >= 1:
            return False
        return True

    if len(s) < k:
        return False
    count = collections.Counter(s)
    temp = list(count.values())
    # print (temp)
    d = collections.defaultdict(list)

    for c in temp:
        flag = 0
        for index in range(k):
            if isallowed(c,d[index]):
                d[index].append(c)
                flag = 1
                break
        if flag == 0:
            return False

    # print (d)
    return True

# print (canConstruct('annabelle',2))
# print (canConstruct('leetcode',3))
# print (canConstruct('true',4))
# print (canConstruct(s = "yzyzyzyzyzyzyzy", k = 2))
# print (canConstruct(s = "cr", k = 7))







import math
def checkOverlap(radius, x_center, y_center, x1,y1,x2,y2):
    if x1 <= x_center <=x2 and y1<= y_center <= y2:
        return True
    for y in range(y1,y2+1):
        if (x_center-x1)**2 + (y_center-y)**2 <= radius**2:
            return True
        if (x_center-x2)**2 + (y_center-y)**2 <= radius**2:
            return True
    for x in range(x1,x2+1):
        if (x_center-x)**2 + (y_center-y1)**2 <= radius**2:
            return True
        if (x_center-x)**2 + (y_center-y2)**2 <= radius**2:
            return True

    return False

# print (checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
# print (checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))
# print (checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))
# print (checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))



