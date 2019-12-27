

def hammingWeight(n):
    s = str(bin(n))
    count = 0
    for x in s:
        if x == '1':
            count += 1
    return count


print (hammingWeight(0b00000000000000000000000000001011))
