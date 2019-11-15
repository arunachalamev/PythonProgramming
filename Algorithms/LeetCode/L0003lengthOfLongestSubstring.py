# Given a string, find the length of the longest substring without repeating characters.



def lengthOfLongestSubstring(s):
    usedCharacterDictionary = {}
    startIndex = 0
    maxLength  = 0

    for index, character in enumerate(s):

        if character in usedCharacterDictionary and startIndex <= usedCharacterDictionary[character]:
            startIndex = usedCharacterDictionary[character] + 1
        else:
            maxLength = max(maxLength,index-startIndex+1)
        
        usedCharacterDictionary[character] = index

    return maxLength

assert (lengthOfLongestSubstring("abcabcbb") == 3)
assert (lengthOfLongestSubstring("bbbbb") == 3)

print ('Done')

