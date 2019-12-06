

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(5), Node(4)), Node(3, Node(7)))


def isComplete(root):
    bfs = [root]
    i = 0
    while bfs[i]:
        bfs.append(bfs[i].left)
        bfs.append(bfs[i].right)
        i +=1
    return not any(bfs[i:])


print (isComplete(tree))