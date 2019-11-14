# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


def addStrings(num1,num2):
    num1 = list(num1)
    num2 = list(num2)

    res, carry = [], 0

    result = ''

    while len(num1)>0 or len(num2)>0:
        d1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
        d2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

        temp = d1 + d2 + carry

        res.append(str(temp%10))

        carry = int(temp/10)

    if carry: res.append(str(carry))

    result =  ''.join(res)

    return result[::-1]


print (addStrings('99','99'))
