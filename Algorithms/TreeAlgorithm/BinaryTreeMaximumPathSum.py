class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2), Node(3))


def maxPathSum(root):

    def max_gain(node):
        nonlocal currentmax
        if node is None:
            return 0

        left_gain = max(max_gain(node.left),0)
        right_gain = max(max_gain(node.right),0)

        newpathsum = node.val + left_gain + right_gain

        currentmax = max(currentmax,newpathsum)

        return node.val + max(left_gain,right_gain)


    currentmax = float('-inf')
    max_gain(root)
    return currentmax

print (maxPathSum(tree))