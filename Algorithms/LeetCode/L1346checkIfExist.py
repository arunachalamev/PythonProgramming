

def checkIfExist(arr):
    mydict = {}
    for i,x in enumerate(arr):
        mydict[x] = i

    for i,x in enumerate(arr):
        if 2*x in mydict and mydict[2*x] != i:
            return True
    return False
    