def preOrder(root):
    if root is None: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def preOrderRecursive(root):
    return [root.val] + preOrderRecursive(root.left) + preOrderRecursive(root.right) if root else []


def inOrder(root):
    if root is None: return []
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def inOrderRecursive(root):
    return inOrderRecursive(root.left) + [root.val] + inOrderRecursive(root.right) if root else []


def postOrder(root):
    if root is None: return []
    stack, output = [root,],[]
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return output[::-1]

def postOrderRecursive(root):
    return postOrderRecursive(root.left) + postOrderRecursive(root.right) + [root.val]  if root else []

import collections
def levelOrder(root):
    levels = []
    if not root:
        return levels

    level = 0
    queue = collections.deque([root,])
    while queue:
        levels.append([])
        level_length = len(queue)
        
        for _ in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    
    return levels



def levelOrderResursive(root):
    levels = []
    if root is None:
        return levels

    def dfs(root, level):
        if root is None:
            return
        if root:
            if level == len(levels):
                levels.append([])
            levels[level].append(root.val)
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)

    dfs(root,0)
    return levels