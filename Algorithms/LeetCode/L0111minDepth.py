class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))

def minDepth(root):
    stack = []
    minDepth = float('inf')
    if root is not None:
        stack.append((root,1))
    
    while stack:
        cur_node, cur_depth = stack.pop()
        if cur_node.left is None and cur_node.right is None:
            minDepth = min (minDepth,cur_depth)
        if cur_node.left: stack.append((cur_node.left, cur_depth+1))
        if cur_node.right: stack.append((cur_node.right, cur_depth+1))

    return(minDepth)

print (minDepth(tree))