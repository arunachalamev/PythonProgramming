class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5, Node(6)))


def countNodes(root):
    def exist(idx,d,root):
        left,right = 0, 2**d - 1
        node = root
        for _ in range(d):
            pivot = left + (right - left)//2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right + 1
                left = pivot
        return node is not None

    if not root: 
        return 0
    
    d = 0
    node = root
    while node.left:
        node = node.left
        d = d + 1
    
    left, right = 1, 2**d -1
    while (left <= right):
        pivot = left + (right -left )//2
        if exist(pivot,d,root):
            left = pivot + 1
        else:
            right = pivot -1

    return 2**d -1 + left


print (countNodes(tree))