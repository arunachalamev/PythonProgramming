
import  random
count = 0
res = 0

def reserviorSampling(item):
    global count, res

    count +=1

    if count == 1:
        res = item
        return res

    else:
        j = int(random.random() * count)
        if j == count - 1:
            res = item
            return res
    return res


stream = [1,2,3,4,5,6,7,8,9]
for index,value in enumerate(stream):
    print(index, reserviorSampling(stream[index]))
