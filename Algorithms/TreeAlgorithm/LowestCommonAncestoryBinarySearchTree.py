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

def LowestCommonAncetoryBST(node, p, q):
    if node is None: return None
    if p < node.val < q:
        return node.val
    if p> node.val and q > node.val:
        return LowestCommonAncetoryBST(node.right,p,q)
    if p < node.val and q < node.val:
        return LowestCommonAncetoryBST(node.left,p,q)
    return -1

print (LowestCommonAncetoryBST(tree, 1, 5))