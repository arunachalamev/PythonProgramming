def maxLength(A):
    dp = [set()]
    for a in A:
        if len(set(a)) != len(a): continue
        a = set(a)
        for c in dp[:]:
            if a & c: continue
            dp.append(a | c)
    return max(len(a) for a in dp)

print (maxLength(["un","iq","ue"]))
print (maxLength(["cha","r","act","ers"]))
