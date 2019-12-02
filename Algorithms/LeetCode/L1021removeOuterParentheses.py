#Remove outermost parrentheses


def removeOuterParentheses(S):
    result = list()
    count = 1
    for ch in S[1:]:
        if ch == '(':
            count = count +1
        elif ch == ')':
            count = count -1
        if ch == '(' and count ==1 :
            continue
        if ch == ')' and count ==0 :
            continue
        result.append(ch)
    return ''.join(result)

print (removeOuterParentheses("(()())(())")) # ()()()
print (removeOuterParentheses("(()())(())(()(()))")) # ()()()()(())
print (removeOuterParentheses("()()")) # NULL
