

def isHappy(n):
    setX = {n}

    while (1):
        sum = 0
        while n > 0:
            sum = sum + (n%10)**2
            n = n //10
        if sum == 1:
            return True
        else:
            if sum in setX:
                return False
            else:
                setX.add(sum)
                n = sum
    return 

print (isHappy(19))
print (isHappy(2))
