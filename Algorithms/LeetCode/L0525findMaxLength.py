

def findMaxLength(nums):
    temp = {0:0}
    maxlen,count = 0,0
    for index,value in enumerate(nums,1):
        if value == 0:
            count -= 1
        elif value == 1:
            count += 1
        if count in temp:
            maxlen = max(maxlen, index - temp[count])
        else:
            temp[count] = index
    
    return maxlen


print (findMaxLength([0,1]))