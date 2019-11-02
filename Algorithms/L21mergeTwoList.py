class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1, node2, node3 = ListNode(1), ListNode(2), ListNode(4)
node1.next, node2.next = node2, node3

l1 = node1


node1, node2, node3 = ListNode(1), ListNode(3), ListNode(4)
node1.next, node2.next = node2, node3

l2 = node1


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


result = mergeTwoLists(l1,l2)

temp = result

while temp:
    print (temp.val)
    temp = temp.next


#Other methods: 2. By recursion, 3. In-place method