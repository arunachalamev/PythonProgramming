
import collections

def minSteps(s,t):

    s1 = collections.Counter(s)
    t1 = collections.Counter(t)

    return sum((t1-s1).values())

print (minSteps("bab","aba"))
print (minSteps("leetcode","practice"))
print (minSteps("anagram","mangaar"))
print (minSteps("xxyyzz","xxyyzz"))
print (minSteps("friend","family"))
print (minSteps("mmm","jjj"))
print (minSteps("gctcxyuluxjuxnsvmomavutrrfb","qijrjrhqqjxjtprybrzpyfyqtzf"))



