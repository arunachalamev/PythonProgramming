

def freqAlphabets(s):
    s = s[::-1]
    i = 0
    result = ''
    while (i <len(s)):
        if s[i] == '#':
            temp = s[i+2] + s[i+1]
            i = i+3
        else:
            temp = s[i]
            i = i+1
        result = result + chr(ord('a')+int(temp)-1)
    return result[::-1]

print (freqAlphabets("10#11#12"))
print (freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
