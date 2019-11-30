
# A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase 
# hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with 
# the letter I.  Such a representation is valid if and only if it consists only of the letters in the set 
# {"A", "B", "C", "D", "E", "F", "I", "O"}.

# Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, 
# otherwise return "ERROR".


def toHexspeak(num):
    if num is None: return 0
    n = int(num)
    res  = list()
    while n > 0:
        res.append(n%16)
        n = n //16
    
    res = res[::-1]
    result = ''
    hexDictionary = {'0':'O', '1':'I','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
    for i in res:
        if 2<=i<=9:
            return "ERROR"
        if i in [0,1,10,11,12,13,14,15]:
            result = result + hexDictionary[str(i)]
        else:
            result = result + str(i)
        

    return result


print (toHexspeak('257'))


