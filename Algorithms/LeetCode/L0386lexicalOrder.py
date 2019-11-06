# Given an integer n, return 1 - n in lexicographical order.

# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


def lexicalOrder1(n):
    newList =[]
    for x in range(1,n+1):
        newList.append(str(x))
    newList.sort()
    return newList

# based on DFS 
#     1
# 10....19
#100...
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




# print (lexicalOrder1(150))   
print (lexicalOrder2(15))