
def subtractProductAndSum(n):
    sum , product = 0,1
    while n>0:
        digit = n%10
        sum = sum + digit
        product = product * digit
        n = n //10
    return product-sum

print (subtractProductAndSum(4421))