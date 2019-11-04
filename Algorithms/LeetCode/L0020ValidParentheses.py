def isValid(s):
    myDict = {"(":")", "[":"]", "{":"}"}
    stack = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            else:
                stackChar = stack.pop()
                if myDict[stackChar] == ch:
                    continue
                else:
                    return False

    if len(stack) == 0:
        return True
    else:
        return False

print (isValid("()"))
print (isValid("()[]{}"))
print (isValid("(]"))
print (isValid("([)]"))
print (isValid("{[]}"))
print (isValid("]"))
