# Vertex cover of binary tree using DP
# https://www.geeksforgeeks.org/vertex-cover-problem-set-2-dynamic-programming-solution-tree/

class Node:
    def __init__(self, val, left=None, right=None , vc=0):
        self.val = val
        self.left = left
        self.right = right
        self.vc = 0


tree = Node(10, Node(20, Node(40), Node(50, Node(70), Node(80))), Node(30, None, Node(60)))

def vertexCover(root):
    if root is None:
        return 0
    
    if not root.left and not root.right:
        return 0

    if root.vc != 0:
        return root.vc

    sizeIncluding = 1 + vertexCover(root.left) + vertexCover(root.right)

    sizeExcluding = 0
    if root.left:
        sizeExcluding += 1 + vertexCover(root.left.left) + vertexCover(root.left.right)
    if root.right:
        sizeExcluding += 1 + vertexCover(root.right.left) + vertexCover(root.right.right)
    
    root.vc = min (sizeIncluding, sizeExcluding)

    return root.vc

print (vertexCover(tree))
