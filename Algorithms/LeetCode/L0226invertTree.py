class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))


def invertTree(root):

    if root is None: return

    left = root.left
    right = root.right

    root.left = invertTree(right)
    root.right = invertTree(left)

    return root

print (invertTree(tree))
