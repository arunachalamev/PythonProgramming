
class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or self.max_stack[-1] <= val:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()
    
    def maxstack(self):
        if not self.stack:
            return None
        return self.max_stack[-1]


s = Stack()
s.push(10)
s.push(12)
s.push(6)
s.push(15)
print (s.maxstack())
s.pop()
print (s.maxstack())
s.pop()
print (s.maxstack())
s.pop()
print (s.maxstack())
s.pop()
print (s.maxstack())

