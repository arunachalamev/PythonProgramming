class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))

#     4
#    / \
#   2   5
#  / \  
# 1   3

def rangeSumBST(root, L,R):
    def preorder(root,result):
        if root is None:
            return
        preorder(root.left,result)
        result.append(root.val)
        preorder(root.right,result)
    
        return result

    result = list()
    preorder(root,result)
    print (result)
    totalSum = 0

    for x in result:
        if L<=x<=R:
            totalSum +=x

    return totalSum

def rangeSumBSTUsingDFS(root,L,R):
    def dfs(root):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if L<=node.val <= R:
                ans += node.val
            if L<=node.val and node.left != None:
                stack.append(node.left)
            if node.val<=R and node.right != None:
                stack.append(node.right)
        return ans

    return dfs(root)


print (rangeSumBST(tree,2,5)) # 14
print (rangeSumBSTUsingDFS(tree,2,5)) # 14
