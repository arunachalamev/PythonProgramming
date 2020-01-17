


def divide(dividend,divisor):
    res = 0
    sign = (dividend < 0) == (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend = dividend - temp
            res += i
            i <<=1
            temp <<=1
    if not sign:
        res =  -1*res
    return min(max(-2147483648, res), 2147483647)


print (divide(10,3))
print (divide(7,-3))
