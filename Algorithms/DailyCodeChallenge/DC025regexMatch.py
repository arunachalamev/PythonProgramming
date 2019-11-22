# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

def regexMatch(text,pattern):
    rows, cols = len(text)+1, len(pattern) + 1

    T = [[False]*cols for _ in range(rows)]

    T[0][0] = True

    for i in range(2,cols):
        if pattern[i-1] == '*':
            T[0][i] = T[0][i-2]

    for i in range(1,rows):
        for j  in range(1,cols):
            if pattern[j-1] == text [i-1] or pattern[j-1] == '.':
                T[i][j] = T[i-1][j-1]
            elif pattern[j-1] == '*':
                T[i][j] = T[i][j-2]
                if pattern[j-2] == '.' or pattern[j-2] == text[i-1]:
                    T[i][j] = T[i][j] | T[i-1][j]
            else:
                T[i][j] = False


    return T[-1][-1]

print (regexMatch('ray','ra.'))
print (regexMatch('','a*b*c'))
print (regexMatch('','a*b*'))
print (regexMatch('chat','.*at'))
print (regexMatch('chats','.*at'))


