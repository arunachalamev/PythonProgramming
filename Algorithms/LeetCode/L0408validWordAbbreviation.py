

def validWordAbbreviation(word, abbr):
    i,j = 0,0
    while (j<len(abbr)):
        count = 1
        if abbr[j].isalpha() and not abbr[j] == word[i]:
            return False
        temp =''
        flag = 0
        while abbr[j].isdigit():
            temp += abbr[j]
            j +=1
            if j >= len(abbr): break
            count = int(temp)
            flag = 1

        i += count
        if flag ==0: j+= 1

    return True

print(validWordAbbreviation('apple','a2e'))
print(validWordAbbreviation('internationalization','i12iz4n'))
print(validWordAbbreviation('internationalization','i5a11o1'))

