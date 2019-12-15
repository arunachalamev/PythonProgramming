

def getDecimalValue(head):
    if head is None: 
        return 0

    temp=''

    while (head):
        temp = temp + str(head.val)
        head = head.next

    return (int(temp,2))
