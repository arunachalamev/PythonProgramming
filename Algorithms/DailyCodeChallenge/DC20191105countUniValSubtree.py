
# Let us construct the below tree 
#         5 
#       /   \ 
#     4      5 
#   /  \      \ 
#  4    4      5 


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1, node2, node3, node4, node5, node6 = Node(5), Node(4), Node(5), Node(4), Node(4), Node(5),

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

def countUniVal(root,count):
    if root is None:
        return True

    leftUniVal = countUniVal(root.left, count)
    rightUniVal = countUniVal(root.right, count)

    if leftUniVal == False or rightUniVal == False:
        return False
    
    if root.left and root.val != root.left.val:
        return False

    if root.right and root.val != root.right.val:
        return False
    
    count[0] = count[0]+1

    return True






def countUniValSubTree(root):
    # To make the variable pass by reference - we use List
    # If it is a normal variable, then it will be pass by value and internal states wont be maintained
    count = [0]

    countUniVal(root,count)

    return count[0]




print (countUniValSubTree(node1))