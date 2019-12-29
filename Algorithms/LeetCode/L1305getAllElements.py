

def getAllElements(root1, root2):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []

    l1 = inorder(root1)
    l2 = inorder(root2)

    return sorted(l1+l2)

