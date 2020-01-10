class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(50, Node(30, Node(20), Node(40)), Node(70, Node(60), Node(80)))

sum = 0
def AddGreaterValueNodeToEveryNode(root):

    def preOrder(node):
        return [node.val] + preOrder(node.right) + preOrder(node.left) if node else []
    
    def addValue(node):
        global sum
        if node:
            addValue(node.right)
            sum = sum + node.val
            node.val = sum
            print (node.val)
            addValue(node.left)
    addValue(root)
    preOrder(root)

print (AddGreaterValueNodeToEveryNode(tree))

