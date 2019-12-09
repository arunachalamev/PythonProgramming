class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))

#     4
#    / \
#   2   5
#  / \  
# 1   3

def lowestCommonAncestor(root,p,q):
    if root is None: return None

    if q.val<root.val and p.val < root.val:
        return lowestCommonAncestor(root.left,p,q)
    elif p.val> root.val and q.val > root.val:
        return lowestCommonAncestor(root.right,p,q)
    else:
        return root.val
    # return None


print (lowestCommonAncestor(tree,Node(1),Node(3)))


def lowestCommonAncestorIterative(root,p,q):
    node = root
    while node:
        if p.val < root.val and q.val < root.val:
            node = node.left
        if p.val > root.val and q.val > root.val:
            node = node.right
        else:
            return node.val


