#  Determine size of the binary Tree

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), None)

def sizeOfBinaryTree(Node):
    if Node is None:
        return 0

    return 1 + sizeOfBinaryTree(Node.left) + sizeOfBinaryTree(Node.right)

print (sizeOfBinaryTree(tree)) #4