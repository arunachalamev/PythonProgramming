def longestCommonPrefix(strs):
    if not strs:
        return ""
    minstr = min(strs,key = len)
    for i,ch in enumerate(minstr):
        for others in strs:
            if others[i] != ch:
                return minstr[:i]
    return minstr


print (longestCommonPrefix(["flower","flow","flight"]))
print (longestCommonPrefix(["dog","racecar","car"]))
