class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))

def binaryTreePaths(node):

    def helper(node,path):
        if node is None: return []
        if node:
            path +=str(node.val)
            if node.left == None and node.right == None:
                paths.append(path)
            else:
                path += '->'
                helper(node.left,path)
                helper(node.right,path)
        return
    
    paths =[]
    helper(node,'')
    return paths

print (binaryTreePaths(tree))


def binaryTreePathsIterative(self, root):
    if not root:
        return []
    
    paths = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.val)))
    
    return paths