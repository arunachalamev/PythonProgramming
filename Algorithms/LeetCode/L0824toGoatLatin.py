# from string import lowercase

def toGoatLatin (S):
    words = S.split(' ')
    result = list()
    i = 1
    for word in words:
        temp = ''.join(['a'] * i)
        if (word[0]).lower() in ['a','e','i','o','u']:
            result.append (word+"ma"+temp)
        else:
            result.append (word[1:]+word[0]+"ma"+temp)
        i +=1
    
    return ' '.join(result)



print (toGoatLatin("I speak Goat Latin"))
print (toGoatLatin("The quick brown fox jumped over the lazy dog"))
print (toGoatLatin("Each word consists of lowercase and uppercase letters only"))