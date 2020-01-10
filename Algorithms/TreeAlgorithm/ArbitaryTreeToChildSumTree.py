class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(50, Node(7, Node(3), Node(5)), Node(2, Node(1), Node(30)))


def ArbitaryTreeToChildSumTree(root):

    def incrementChild(node,increment):
        if node is None or (node.left is None and node.right is None):
            return
        if node.left:
            node.left.val = node.left.val + increment
            incrementChild(node.left,increment)
        else:
            node.right.val = node.right.val + increment
            incrementChild(node.right,increment)
        return


    def toChildSumTree(node):
        if node is None:
            return
        if not node.left and not node.right:
            return node.val
        
        sum1 = toChildSumTree(node.left)
        sum2 = toChildSumTree(node.right)

        if node.val < sum1 + sum2:
            node.val = sum1 + sum2
        elif node.val > sum1 + sum2:
            incrementChild(node,node.val-sum1-sum2)
        return node.val

    toChildSumTree(root)

def Inorder(node):
    return Inorder(node.left) + [node.val] + Inorder(node.right) if node else []

print (Inorder(tree))
print (ArbitaryTreeToChildSumTree(tree))
print (Inorder(tree))
