class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(3, Node(4, Node(1), Node(3)), Node(5, Node(1)))

def rob(node):
    if node is None: return 0

    val = 0
    if node.left is not None:
        val += rob(node.left.left) + rob(node.left.right)
    if node.right is not None:
        val += rob(node.right.left) + rob(node.right.right)
    
    return max(val+node.val , rob(node.left)+ rob(node.right))


print (rob(tree))