# Given an integer n, return 1 - n in lexicographical order.
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

# The idea is pretty simple. If we look at the order we can find out we just 
# keep adding digit from 0 to 9 to every digit and make it a tree.
# 
#        1        2        3    ...
#       /\        /\       /\
#    10 ...19  20...29  30...39   ....

def lexicalOrder2(n):
    def dfs(k,res):
        if k<=n:
            res.append(k)
            t = 10 * k
            if t <=n:
                for i in range(10):
                    dfs(t+i,res)

    res=[]
    for i in range(1,10):
        dfs(i,res) # call dfs(1,res) , dfs(2,res)...dfs(9,res) - res is passed by reference
    return res


def lexicalOrder1(n):
    newList =[]
    for x in range(1,n+1):
        newList.append(str(x))
    newList.sort()
    return newList

# print (lexicalOrder1(150))   
print (lexicalOrder2(15))