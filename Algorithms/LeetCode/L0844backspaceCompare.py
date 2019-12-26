

def backspaceCompare(S,T):
    temp1, temp2  = [], []
    for x in S:
        if x!='#':
            temp1.append(x)
        else:
            if temp1: temp1.pop()
    
    for x in T:
        if x!='#':
            temp2.append(x)
        else:
            if temp2: temp2.pop()

    return temp1 == temp2

print (backspaceCompare("ab#c","ad#c"))
print (backspaceCompare("ab##","c#d#"))
print (backspaceCompare("a##c","#a#c"))
print (backspaceCompare("a#c","b"))
