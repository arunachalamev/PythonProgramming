class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(3), Node(4)),Node(2, Node(4), Node(3)))


def isBalanced(root):
    
    def height(node):
        if node is None:
            return 0
        return max(height(node.left),height(node.right))+1

    if root:
        leftTreeNodeHeight = height(root.left)
        rightTreeNodeHeight = height(root.right)
        if abs(leftTreeNodeHeight-rightTreeNodeHeight) <= 1 and isBalanced(root.left) and isBalanced(root.right):
            return True
        else:
            return False
    else:
        return True


print (isBalanced(tree))