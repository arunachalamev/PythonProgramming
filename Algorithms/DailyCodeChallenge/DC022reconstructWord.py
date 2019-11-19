
def reconstructWord(words, string):
    wordset = set(words)
    temp = ''

    result = list()

    for index,char in enumerate(string):
        temp  = temp + char

        if temp in wordset:
            result.append(temp)
            temp = ''
    
    if temp == '':
        return result
    else:
        return None


dictionary = ['quick', 'brown', 'the', 'fox']
string = "thequickbrownfox"


print (reconstructWord(dictionary,string))
