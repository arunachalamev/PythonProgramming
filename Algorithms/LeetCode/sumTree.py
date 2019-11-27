class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(26, Node(10, Node(4), Node(6)), Node(3, None, Node(3)))


def sumNode(Node):
    if Node is None:
        return 0
    return sumNode(Node.left) + Node.val + sumNode(Node.right)


def isSumTree(Node):
    if Node == None or (Node.left == None and Node.right == None):
        return True
    
    left = sumNode(Node.left)
    right = sumNode(Node.right)

    if Node.val == left + right and isSumTree(Node.left) and isSumTree(Node.right):
        return True

    return False

print (isSumTree(tree))