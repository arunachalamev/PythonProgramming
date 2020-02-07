class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))


def inorderSuccessor(root,p):

    if p.right:
        p = p.right
        while p.left:
            p=p.left
        return p

    stack, prev = [], float('-inf')

    while stack:

        while root:
            root = root.left
            stack.append(root)
        
        root = stack.pop()
        if prev == p.val:
            return root
        prev = root.val
        root = root.right
    
    return None

# print (inorderSuccessor(tree,Node(3)))