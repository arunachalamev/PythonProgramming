def printVertically(s):
    string = s.split(' ')
    maxlen = 0
    for word in string:
        maxlen = max(maxlen, len(word))

    for i in range(len(string)):
        string[i] = string[i].ljust(maxlen)

    mydict = [[] for _ in range(maxlen)]
    for word in string:
        for index, value in enumerate(word):
            mydict[index].append(value)
    result = []
    for i in range(len(mydict)):
        result.append((''.join(mydict[i]).rstrip()))
    return result


print (printVertically("HOW ARE YOU"))
