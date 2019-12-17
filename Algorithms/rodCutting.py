

def rodCutting(price,totallength):

    temp = [0]*(len(price)+1)


    for i in range(1,len(price)+1):
        for j in range(i,len(price)+1):
            temp[j] = max(temp[j] , temp[j-i]+price[i-1])
        print (temp)
        
    return None

print(rodCutting([2,5,7,8],5))