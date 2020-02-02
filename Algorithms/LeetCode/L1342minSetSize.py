import collections

def minSetSize(arr):
    size = len(arr)
    count = collections.Counter(arr)
    target = size//2
    new = {k: v for k, v in sorted(count.items(), key=lambda x: -x[1])}
    removedcount = 0
    for k,v in new.items():
        size = size - v
        removedcount +=1
        if size <= target:
            return removedcount

    return 0


print (minSetSize([3,3,3,3,5,5,5,2,2,7]))

#output: 2