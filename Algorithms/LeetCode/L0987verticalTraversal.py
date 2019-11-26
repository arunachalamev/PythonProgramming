class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6, None , Node(8)), Node(7, None , Node(9))))

import collections

def verticalTraversal(root):
    g = collections.defaultdict(list) 
    queue = [(root,0)]
    while queue:
        new = []
        d = collections.defaultdict(list)
        for node, s in queue:
            d[s].append(node.val) 
            if node.left:  new += (node.left, s-1), 
            if node.right: new += (node.right,s+1),  
        for i in d: g[i].extend(sorted(d[i]))
        queue = new
    return [g[i] for i in sorted(g)]

print(verticalTraversal(tree))