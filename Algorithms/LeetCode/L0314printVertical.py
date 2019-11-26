class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6, Node(None), Node(8)), Node(7, Node(None), Node(9))))

#     1
#    / \
#   2   3
#  / \ /  \
# 4  5 6   7
#       \   \ 
#        8   9

import collections

def populateMap(root,level, hd):
    if not root:
        return None
    
    hd[level].append(root.val)
    populateMap(root.left,level-1,hd)
    populateMap(root.right,level+1,hd)

    return None

def printVertically(root):
    hd = collections.defaultdict(list)

    populateMap(root,0,hd)

    for value in sorted(hd):
            print (hd[value])
    
    return None

print (printVertically(tree))