
def sequentialDigits(low,high):
    l1 = ['1','2','3','4','5','6','7','8','9']

    n1 = len(str(low))
    n2 = len(str(high))
    i = n1
    result = []
    while (i<=n2):
        for j in range (10-i):
            cand = int(''.join(l1[j:j+i]))
            if low <= cand <= high:
                result.append(cand)
        i +=1

    return result