# Given a non-empty string containing an out-of-order English representation of digits 0-9, 
# output the digits in ascending order.

# Input: "fviefuro"
# Output: "45"

def originalDigits(s):
    res =[]
    count = [0]*10
    for c in s:
        if c == 'z' : count[0] = count[0] + 1
        if c == 'w' : count[2] = count[2] + 1
        if c == 'u' : count[4] = count[4] + 1
        if c == 'x' : count[6] = count[6] + 1
        if c == 'g' : count[8] = count[8] + 1
        if c == 'o' : count[1] = count[1] + 1 
        if c == 'h' : count[3] = count[3] + 1 
        if c == 'f' : count[5] = count[5] + 1 
        if c == 's' : count[7] = count[7] + 1 
        if c == 'i' : count[9] = count[9] + 1 

    count[1] = count[1] - count[0] - count[2] - count[4]
    count[3] = count[3] - count[8]
    count[5] = count[5] - count[4]
    count[7] = count[7] - count[6]
    count[9] = count[9] - count[6] - count[5] - count[8]

    for i in range(10):
        while count[i] >0:
            res.append(str(i))
            count[i] = count[i] -1

    return ''.join(res)

print (originalDigits("fviefuro"))
print (originalDigits("owoztneoer"))

    