
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

s = Node(4, Node(2, Node(1), Node(3)), Node(5))
t = Node(2, Node(1), Node(4))


def isSubTree(s,t):
    def equals(s,t):
        if not s and not t:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and equals(s.left,t.left) and equals(s.right,t.right)

    def traverse(s,t):
        return s is not None and ( equals(s,t) or traverse(s.left,t) or traverse(s.right,t))

    return traverse(s,t)





print (isSubTree(s,t))


