# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# 	• is_locked, which returns whether the node is locked
# 	• lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
# 	• unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you would like. 
# You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
# Each method should run in O(h), where h is the height of the tree.


def isParentLocked(node):
    if not node.parent:
        return False
    elif node.parent.locked:
        return True
    return isParentLocked(node.parent)

def updateParent(node, lockStatus):
    increament = 1 if lockStatus else -1
    if node.parent:
        node.parent.lockedDescentantCount += increament
        updateParent(node.parent,lockStatus)

class lockedBinaryTree:
    def __init__ (self, val, parent):
        self.val = val
        self.parent = parent
        self.locked = False
        self.lockedDescentantCount = 0

    def __str__(self):
        return "val={}, locked={}, lockedDescentantCount={}".format(self.val,self.locked,self.lockedDescentantCount)

    def islocked(self):
        return self.locked

    def lock(self):
        if self.lockedDescentantCount or isParentLocked(self):
            return False
        else:
            self.locked = True
            updateParent(self,True)
            return True
    
    def unlock(self):
        if self.lockedDescentantCount or isParentLocked(self):
            return False
        else:
            self.locked = False
            updateParent(self,False)
            return True



a = lockedBinaryTree("a", None)
b = lockedBinaryTree("b", a)
c = lockedBinaryTree("c", a)
d = lockedBinaryTree("d", b)
e = lockedBinaryTree("e", b)
f = lockedBinaryTree("f", c)
g = lockedBinaryTree("g", c)

print( b.lock() )
print( b.islocked() )
print( c.lock() )
print( b.unlock() )
print( not b.islocked() )
print( d.lock() )

print( not g.lock() )
print( c.unlock() )
print( g.lock() )

print( f.lock() )
print( e.lock() )
print( a )
print( b.lockedDescentantCount )
print( c.lockedDescentantCount )