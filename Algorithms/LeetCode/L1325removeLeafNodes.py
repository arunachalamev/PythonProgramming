

def removeLeafNodes(node,target):
    if node:
        node.left = removeLeafNodes(node.left, target)
        node.right = removeLeafNodes(node.right, target)
        if node.val == target and node.left is None and node.right is None:
            return None
        return node
