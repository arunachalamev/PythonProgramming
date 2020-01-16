class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def BinaryTreeFromParentRepresentation(nums):
    t = []
    for i in range(len(nums)):
        x = Node(i)
        t.append(x)
    
    for index,value in enumerate(nums):
        if value == -1:
            root = t[index]
            continue
        parent = t[value]
        if parent.left == None:
            parent.left = t[index]
        else:
            parent.right = t[index]
    return root
    
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

print (inorder(BinaryTreeFromParentRepresentation([1, 5, 5, 2, 2, -1, 3])))
