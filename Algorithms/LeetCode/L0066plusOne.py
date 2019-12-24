

def plusOne(digits):
    temp =''
    for x in digits:
        temp += str(x)
    
    value = int(temp)+1
    value = str(value)
    result = []

    for x in value:
        result.append(x)

    return result

print (plusOne([4,3,2,1]))