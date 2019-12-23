# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

def letterCasePermutation(S):

    result = [[]]

    for char in S:
        n = len(result)
        for i in range(n):
            if char.isalpha():
                result.append(result[i][:])
                result[i].append(char.lower())
                result[n+i].append(char.upper())

            else:
                result[i].append(char)


    return list(map("".join, result))

print (letterCasePermutation('a1b2'))