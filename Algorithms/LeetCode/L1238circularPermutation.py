def circularPermutation(n, start):

    binaryList = list(map(binaryToGray,range(2**n))) # Construct gray code for n 
    
    print (binaryList)

    index = binaryList.index(start) # find the position of start
 
    return binaryList[index:] + binaryList[:index] # arrange the array according to start

def binaryToGray(n):
    return (n ^ n >>1) # method to find gray code for n


print (circularPermutation(2,3))




