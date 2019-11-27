# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def sortedArrayToBst(Array,low,high):
    if low > high:
        return None

    mid = (low + high) // 2

    x = Node(Array[mid])
    x.left = sortedArrayToBst(Array,low, mid-1)
    x.right = sortedArrayToBst(Array,mid+1,high)    
    return x

print(sortedArrayToBst([-10,-3,0,5,9],0,4))

