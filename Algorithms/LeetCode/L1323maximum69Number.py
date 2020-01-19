

def maximum69Number (num):
    temp =''
    index = 0
    for i in list(str(num)):
        if i == '6' and index == 0:
            temp = temp + '9'
            index = 1
        else:
            temp = temp + i
    return temp


print (maximum69Number(9669))
print (maximum69Number(9996))
