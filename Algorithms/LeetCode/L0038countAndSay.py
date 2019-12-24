# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

def countAndSay(n):
    if n==1: return "1"
    current = "1"

    count =1
    for _ in range(n-1):
        current += '#'
        temp =''
        for index in range(len(current)-1):
            if current[index] == current[index+1]:
                count +=1
                continue
            else:
                temp = temp + str(count) + current[index]
                count = 1
        current = temp
    
    return temp



print (countAndSay(5))