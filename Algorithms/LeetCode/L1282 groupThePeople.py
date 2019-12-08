import collections

def groupThePeople(groupSizes):
    myDict = collections.defaultdict(list)
    index = 0
    for x in groupSizes:
        myDict[x].append(index)
        index = index + 1

    # print (myDict)
    list_values = [ [k,v] for k,v in myDict.items() ]
    # print (list_values)

    result = []

    for size,mylist in list_values:
        if len(mylist) == size:
            result.append(mylist)
        else:
            for i in range(0, len(mylist), size):
                result.append(mylist[i:i + size])

    return result
    
print (groupThePeople([3,3,3,3,3,1,3]))