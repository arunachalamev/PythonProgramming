class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))


def closestValue(root,target):

    def traverse(r):
        return traverse(r.left) + [r.val] + traverse(r.right) if r else []

    l = traverse(root)
    print (l)
    minX = float('inf')
    for x in l:
        if abs(x-target)<minX:
            value = x
            minX = abs(x-target)

    return value

print (closestValue(tree,3.71))


