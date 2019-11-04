

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5


def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    def callSerialize(root):
        if (not root): 
            array.append ('X')
        else:
            array.append(str(root.val))
            callSerialize(root.left)
            callSerialize(root.right)

    array = []
    callSerialize(root)
    return (' '.join(array))
    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    def callDesrialize():
        val = next(x)
    
        if val == 'X' :
            return None

        node = TreeNode (int(val))
        node.left = callDesrialize()
        node.right = callDesrialize()
        return node

    x = iter(data.split())
    return  callDesrialize()


print (serialize(node1))

print(deserialize("1 2 X X 3 4 X X 5 X X"))

