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

def rightSideViewByLevelOrder(root):
    view = []
    if root:
        level = [root]
        while level:
            view  += level[-1].val,
            level = [child for node in level for child in (node.left, node.right) if child]
    return view

def rightSideViewByRecursive(root):

    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right,depth + 1)
            collect(node.left, depth + 1)

    view = []
    collect(root,0)
    return view

print (rightSideViewByLevelOrder(tree))
print (rightSideViewByRecursive(tree))
