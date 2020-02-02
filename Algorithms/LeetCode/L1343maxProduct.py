class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(4, Node(2, Node(1), Node(3)), Node(5))



def maxProduct(root):
    mod = 10**9 + 7
    s,ans = 0, 0
    def dfs(node):
        nonlocal s
        if node:
            s = s + node.val
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    
    def dfs2(node):
        nonlocal s, ans
        if not node: return 0
        st = node.val + dfs2(node.left) + dfs2(node.right)
        cand = st * (s - st)
        if cand>ans: ans = cand
        return st

    dfs2(root)
    # print (ans)

    return ans % mod

print (maxProduct(tree))