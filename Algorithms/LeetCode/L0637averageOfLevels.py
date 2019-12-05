class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(3, Node(9), Node(20, Node(15), Node(7)))

import collections

def averageOfLevels(root):
    if not root:
        return []

    queue = collections.deque()

    queue.append(root)
    queue.append ('|')
    result = [root.val]
    temp = []
    while queue :
        currentNode = queue.popleft()
        if currentNode == '|':
            if len(temp):
                queue.append('|')
                result.append(sum(temp)/len(temp))
                temp = []
            else:
                break

        else:
            if currentNode.left: 
                queue.append(currentNode.left) 
                temp.append(currentNode.left.val)
            if currentNode.right: 
                queue.append(currentNode.right)
                temp.append(currentNode.right.val)

    # print (result)
    return result

averageOfLevels(tree)

