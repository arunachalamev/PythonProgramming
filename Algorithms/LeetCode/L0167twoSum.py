

def twoSum(numbers,target):
    i,j = 0, len(numbers)-1
    while (i<j):
        sumX = numbers[i] + numbers[j]
        if sumX == target:
            return (i+1,j+1)
        elif sumX < target:
            i += 1
        else:
            j -= 1
    
    return

print (twoSum([2,7,11,15],9))

