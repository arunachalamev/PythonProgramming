

def numJewelsInStones(J,S):
    j = set(J)
    count = 0
    for s in S:
        if s in j:
            count +=1
    return count

print(numJewelsInStones('aA','aAAbbbb'))
print(numJewelsInStones('z','ZZ'))

