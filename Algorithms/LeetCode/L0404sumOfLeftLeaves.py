class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

root = Node(3, Node(9), Node(20,Node(15),Node(7)))

def sumOfLeftLeaves(root):
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)

    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)


def sumOfLeftLeaves2(root):
    sum = [0]
    def dfs(root):
        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            sum[0] = sum[0] + root.left.val

        dfs(root.left)
        dfs(root.right)
        return sum[0]

    dfs(root)
    return sum[0]


print (sumOfLeftLeaves(root))
print (sumOfLeftLeaves2(root))
