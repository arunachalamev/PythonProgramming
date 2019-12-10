
def isStrobogrammatic(num):
    result = []
    myDict ={'0':'0','8':'8','6':'9','9':'6'}
    for x in num:
        if x in '123457':
            return False
        else:
            result.append(myDict[x])
    result = result[::-1]
    if num == ''.join(result):
        return True
    else:
        return False

print (isStrobogrammatic("69"))
print (isStrobogrammatic("962"))
print (isStrobogrammatic("88"))
