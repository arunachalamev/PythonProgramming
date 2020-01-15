

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1, Node(2, Node(3), Node(4)), Node(5))

def preorder(root):
    if root is None: return []
    stack, output = [root,],[]
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return output

def postorder(root):
    if root is None: return []
    stack, output = [root,],[]
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return output[::-1]

def inorder(root):
    if root is None: return []
    stack, result = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if len(stack)==0:
            return result
        node = stack.pop()
        result.append(node.val)
        root = node.right
    return

def preorderRec(node):
    return [node.val] + preorderRec(node.left) + preorderRec(node.right) if node else []

def inorderRec(node):
    return inorderRec(node.left) + [node.val] + inorderRec(node.right) if node else []

def postorderRec(node):
    return postorderRec(node.left) + postorderRec(node.right) + [node.val] if node else []

print (preorder(tree))
print (inorder(tree))
print (postorder(tree))

print (preorderRec(tree))
print (inorderRec(tree))
print (postorderRec(tree))

