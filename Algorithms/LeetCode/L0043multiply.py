

def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    position = len(product)-1

    for x in num1[::-1]:
        temp = position
        for y in num2[::-1]:
            product[temp] += int(x) * int(y)
            product[temp-1] += product[temp] // 10
            product[temp] = product[temp] %10
            temp -=1
        position -= 1
    
    print (product)

    pos = 0
    while pos<len(product)-1 and product[pos] ==0:
        pos += 1
    
    return ''.join(map(str,product[pos:]))

print (multiply('12','11'))
