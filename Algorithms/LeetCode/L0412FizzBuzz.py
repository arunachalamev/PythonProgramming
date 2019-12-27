
def fizzBuzz(n):
    result = []

    for x in range(1,n+1):
        temp = ''
        if x%3 == 0: 
            temp = temp + 'Fizz'
        if x%5 == 0:
            temp = temp + 'Buzz'
        if x%3 !=0 and x%5 !=0:
            temp = str(x)
        
        result.append(temp)
    
    return result


print (fizzBuzz(15))