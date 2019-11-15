# Given a binary tree, determine if it is a valid binary search tree (BST).

import math


class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree1 = Node(2, Node(1), Node(3))
tree2 = Node(5, Node(1), Node(4, Node(3), Node(6)))


def isValidBSTUtil(root, mini, maxi):
    if not root:
        return True
    
    if root.val < mini or root.val > maxi:
        return False

    return isValidBSTUtil(root.left, mini, root.val-1) and isValidBSTUtil(root.right, root.val+1, maxi)


def isValidBST(root):
    if isValidBSTUtil(root, -math.inf, math.inf):
        return True
    else:
        return False


print (isValidBST(tree1))
print (isValidBST(tree2))
