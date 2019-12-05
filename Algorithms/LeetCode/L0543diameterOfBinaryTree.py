class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(4), Node(5)), Node(3))

def diameterOfBinaryTree(root):
    if root is None:
        return 0

    def depth(node):
        if node is None:
            return 0
        return 1+ max(depth(node.left),depth(node.right))

    depthLeft = depth(root.left)
    depthRight = depth(root.right)

    ldiameter = diameterOfBinaryTree(root.left)
    rdiameter = diameterOfBinaryTree(root.right)

    return max(depthLeft+depthRight+1, max(ldiameter,rdiameter)) - 1



print (diameterOfBinaryTree(tree))