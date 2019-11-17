# You are given an even number of people num_people that stand around a circle 
# and each person shakes hands with someone else, so that there are num_people / 2 handshakes total.
# Return the number of ways these handshakes could occur such that none of the handshakes cross.
# Since this number could be very big, return the answer mod 10^9 + 7

def numberOfWays(num_people):
    resultDict = {0:1}
    res = 0

    if num_people<0 or num_people%2 == 1:
        return 0

    if num_people in resultDict:
        return resultDict[num_people]

    for i in range(1,num_people):
        a = i - 1 
        b = num_people - (i + 1)
        res = res + numberOfWays(a) * numberOfWays(b)
        res = res % (10**9 + 7)
        resultDict[i] = res
    
    return res


assert (numberOfWays(2) == 1)
assert (numberOfWays(4) == 2)

print ('done')

