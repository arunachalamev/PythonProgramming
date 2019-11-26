# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

node1 = Node(1, Node(2), Node(3))
node2 = Node(1, Node(2), Node(3))

def sameTree(node1, node2):
    if not node1 and not node2:
        return True
    
    if not node1 or not node2:
        return False

    return node1.val == node2.val and sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)


print (sameTree(node1,node2))

node1 = Node(1, Node(2), Node(3))
node2 = Node(1, Node(2), Node(0))

print (sameTree(node1,node2))
