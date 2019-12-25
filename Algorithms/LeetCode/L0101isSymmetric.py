class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(3), Node(4)),Node(2, Node(4), Node(3)))


def isSymmetric(root):
    return isMirror(root,root)

def isMirror(t1,t2):
    if t1 == None and t2 == None: return True
    if t1 == None or t2 == None: return False
    return t1.val == t2.val and isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)

print (isSymmetric(tree))


