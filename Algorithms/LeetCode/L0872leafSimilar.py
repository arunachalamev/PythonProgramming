
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

root1 = Node(4, Node(2, Node(1), Node(3)), Node(5))
root2 = Node(4, Node(3, Node(1), Node(3)), Node(5))
root3 = Node(4, Node(2, Node(1), Node(3)), Node(6))

root4 = Node(3, Node(5, Node(6), Node(2, Node(7), Node(4))), Node(1, Node(9),Node(8)))

import collections
def leafSimilar(root1, root2):

    temp1, temp2 = [], []
    q1 = [root1]
    while q1:
        node = q1.pop()
        if node.left is None and node.right is None:
            temp1.append(node.val)
        if node.right: q1.append(node.right)
        if node.left: q1.append(node.left)
        
    q2= [root2]
    while q2:
        node = q2.pop()
        if node.left is None and node.right is None:
            temp2.append(node.val)
        if node.right: q2.append(node.right)
        if node.left: q2.append(node.left)
        

    print (temp1,temp2)
    if temp1== temp2: 
        return True
    else: return False

def leafSimilarrecursion(root1,root2):
    def dfs(node):
        if node:
            if node.left is None and node.right is None:
                yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)

    return list(dfs(root1)) == list(dfs(root2))

print (leafSimilarrecursion(root1, root2))
print (leafSimilarrecursion(root1, root4))
