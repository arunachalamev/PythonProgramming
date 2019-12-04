
# X is a good number if after rotating each digit individually by 180 degrees, 
# we get a valid number that is different from X.  Each digit must be rotated - 
# we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. 
# 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, 
# and the rest of the numbers do not rotate to any other number and become invalid.

# Now given a positive number N, how many numbers X from 1 to N are good?

def rotatedDigits(N):

    myDict = {'1':'1','2':'5','5':'2','6':'9','8':'8','9':'6','0':'0'}
    count = 0
    for i in range(1,N+1):
        temp = str(i)
        result = ''
        flag = 1
        for ch in temp:
            if ch not in myDict:
                flag = 0
                break
            else:
                result = result + myDict[ch]
        if flag == 1 and int(result) != i:
            count = count + 1
    return count


print (rotatedDigits(10)) #4


# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.