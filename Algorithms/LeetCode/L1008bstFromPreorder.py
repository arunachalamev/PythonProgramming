class BST:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makelist(node):
    if node is None:
        return []
    return makelist(node.left) + [node.val] + makelist(node.right)

def bstFromPreorder(preorder):
    def helper (lower,upper):
        nonlocal index
        if index == len(preorder):
            return None

        val = preorder[index]
        if val<lower or val>upper:
            return None

        index += 1
        node = BST(val)
        node.left = helper(lower,val)
        node.right = helper(val,upper)
        return node

    index = 0

    return helper(-float('inf'),float('inf'))

print (makelist(bstFromPreorder([8,5,1,7,10,12])))

