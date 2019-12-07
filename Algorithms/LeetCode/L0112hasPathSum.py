class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))


#9

def hasPathSum(root, sum):
    if not root:
        return sum==0
    stack = [(root,root.val)]
    while stack:
        curNode, curSum = stack.pop()
        if curSum == sum and not curNode.left and not curNode.right:
            return True
        if curNode.left: stack.append((curNode.left, curSum+curNode.left.val))
        if curNode.right: stack.append((curNode.right, curSum+curNode.right.val))
    
    return False

print (hasPathSum(tree,9))
print (hasPathSum(Node(1,Node(2)),1))



def hasPathSum1(root, sum):
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:  # if reach a leaf
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

