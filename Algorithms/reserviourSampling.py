import random

def reservior(k,n):
    samplingList = [0]*k
    i =0
    #copy first k elements
    while i<k:
        samplingList[i] = i
        i = i + 1

    for i in range(k,n):
        j = int(random.random()*i)

        # if the generated random number lies between 0 and k, replace the element
        if 0<=j<k:
            samplingList[j] = i
    
    return samplingList

print (reservior(10,10))
print (reservior(10,50))
