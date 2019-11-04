def reorderLogFiles(logs):
    letterlogs, digitlogs = [], []

    for x in logs:
        words = x.split()
        if words[1].isdigit():
             digitlogs.append(x)
        else:
            letterlogs.append(x)

    letterlogs.sort(key= lambda x: (x.split())[1:]+[(x.split())[0]])

    return letterlogs + digitlogs


print (reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print (reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print (reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))
