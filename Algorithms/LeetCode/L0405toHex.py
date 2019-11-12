def toHex(num):
    result =""
    mappingDict = {'10':'a','11':'b','12':'c','13':'d','14':'e','15':'f'}
    while num%16 > 0:
        rem = num % 16
        if rem <10:
            result = str(rem)+result
        else:
            temp = str(rem)
            result = mappingDict[temp] + result
        
        num = num//16

    return result

def toHex2(num):
    if num ==0 : return 0
    mp = '0123456789abcdef'
    ans = ''
    for _ in range(8): #for 32 bit 
        rem = num & 15
        char = mp[rem]
        ans = char + ans
        num = num >>4
    return ans.lstrip('0')

print (toHex(26))
print (toHex2(26))
print (toHex2(-1))

