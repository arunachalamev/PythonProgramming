# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

def minRemoveToMakeValid(s):
    pos = []
    remove = []
    for i in range(len(s)):
        if s[i] == "(":
            pos.append(i)
        if s[i] == ")":
            if (len(pos)<=0):
                remove.append(i)
            else: pos.pop()
    
    while (len(pos)>0):
        remove.append(pos.pop())
    
    result = "".join(s[i] for i in range(len(s)) if i not in remove)
    return (result)


print (minRemoveToMakeValid("lee(t(c)o)de)"))
print (minRemoveToMakeValid(")))((("))
print (minRemoveToMakeValid("a)b(c)d"))


