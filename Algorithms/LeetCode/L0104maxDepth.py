class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2), Node(5))

def maxDepth(root):
    if root is not None:
        maxdepth = [1]
    else:
        maxdepth = [0]
    def maxdepthhelper(node,d):
        if node is None:
            return
        maxdepth[0] = max(maxdepth[0],d)
        maxdepthhelper(node.left,d+1)
        maxdepthhelper(node.right,d+1)
        return


    maxdepthhelper(root,1)
    return maxdepth[0]

print (maxDepth(tree))

#Recursive
def maxDepth1(self, root):
    if root is None: 
        return 0 
    else: 
        left_height = self.maxDepth(root.left) 
        right_height = self.maxDepth(root.right) 
        return max(left_height, right_height) + 1 

#Iteration
def maxDepth2(self, root):
    stack = []
    if root is not None:
        stack.append((1, root))
    
    depth = 0
    while stack != []:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))
    
    return depth