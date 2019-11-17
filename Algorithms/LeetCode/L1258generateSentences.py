# Given a list of pairs of equivalent words synonyms and a sentence text, 
# Return all possible synonymous sentences sorted lexicographically.

# Input:
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# Output:
# ["I am cheerful today but was sad yesterday",
# ​​​​​​​"I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]


import collections
import itertools
def generateSentences(synonyms, text):

    def dfs(word):
        for nei in graph[word]:
            if nei not in seen:
                seen.add(nei)
                dfs(nei)
    
    graph = collections.defaultdict(list)

    for u,v in synonyms:
        graph[u].append(v)
        graph[v].append(u)

    A = text.split(' ')
    B = []

    for word in A:
        if word not in graph:
            B.append([word])
            continue
        else:
            seen = {word}
            dfs(word)
            B.append(list(seen))
    
    ans = []
    for can in itertools.product(*B):
        ans.append(" ".join(can))

    ans.sort()

    return ans


synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"

print(generateSentences(synonyms,text))