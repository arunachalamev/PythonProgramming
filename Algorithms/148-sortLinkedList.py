# Create Linked list with required elements
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1, node2, node3 , node4 = ListNode(4), ListNode(2), ListNode(1), ListNode(3)
node1.next, node2.next, node3.next = node2, node3, node4

head = node1

temp = head
while temp:
    print (temp.val)
    temp = temp.next


#Merge two linked list
def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    
    dummy = ListNode(0)
    cur = ListNode(0)
    dummy = cur

    while (l1 and l2):
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next

        elif l1.val >= l2.val:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2

    return dummy.next


#Sort original linked list - Divide and conqure strategy
def sortList(head):
    if not head or not head.next:
        return head
    
    prev,slow,fast = None, head, head

    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next

    prev.next = None

    first_half = sortList(head)
    second_half = sortList(slow)

    mergedList = mergeTwoLists(first_half,second_half)

    return mergedList


#Call the function
result = sortList(head)
temp = result
print ('Output')
while temp:
    print (temp.val)
    temp = temp.next