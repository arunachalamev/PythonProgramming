def readBinaryWatch(n):
    result = list()
    for h in range(0,13):
        for m in range(0,60):
            if (bin(h) + bin(m)).count('1') == n:
                temp = str(h) + ":" + str(m)
                result.append([temp])
    return result

print (readBinaryWatch(1))