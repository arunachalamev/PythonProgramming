

def convertToTitle(n):
    temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    # if n<=26 : return temp[n%26]
    while n>0:
        rem = (n-1) % 26
        n  = (n-1) // 26
        result.append(temp[rem])
    return ''.join(result[::-1])

print (convertToTitle(27))