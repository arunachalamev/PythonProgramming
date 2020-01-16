

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(20, Node(8,Node(4),Node(12, Node(10), Node(14))), Node(22, None, Node(25)))

def printBoundary(node):

    def printLeftBoundary(node):
        if node:
            if node.left:
                print (node.val)
                printLeftBoundary(node.left)
            elif node.right:
                print (node.val)
                printLeftBoundary(node.right)

    def printRightBoundary(node):
        if node:
            if node.right:
                printRightBoundary(node.right)
                print(node.val)
            elif node.left:
                printRightBoundary(node.left)
                print(node.val)

    def printLeaves(node):
        if node:
            printLeaves(node.left)
            if node.left is None and node.right is None:
                print (node.val)
            printLeaves(node.right)

    if node:
        print (node.val)
        printLeftBoundary(node.left)
        printLeaves(node.left)
        printLeaves(node.right)
        printRightBoundary(node.right)

        return

printBoundary(tree)