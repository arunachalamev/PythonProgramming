def reverseInteger(num):
    result, negative_flag = 0, 0
    if num < 0 :
        negative_flag = 1
        num = abs(num)

    while num > 0 :
        result = result * 10 + num % 10
        num =  num//10
    
    if negative_flag : result = -1*result

    if result > 2**31 -1 or result < -2**31:
        return 0
    else: 
        return result

print (reverseInteger(1534236469))
