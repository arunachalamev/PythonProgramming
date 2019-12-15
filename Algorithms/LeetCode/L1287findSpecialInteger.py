import collections

def findSpecialInteger(arr):
    s = collections.Counter(arr)
    # print (s)

    for i in arr:
        print (i)
        if s[i] >= len(arr)/4:
            return i

    return None

print (findSpecialInteger([1,2,2,6,6,6,6,7,10]))