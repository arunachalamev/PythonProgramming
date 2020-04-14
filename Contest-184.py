

def function(words):
    res = set()
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] in words[j]:
                res.add(words[i])
                continue
            if words[j] in words[i]:
                res.add(words[j])
                continue
    return list(res)

# print(function(["mass","as","hero","superhero"]))
# print(function(["leetcode","et","code"]))
# print(function(["blue","green","bu"]))
# print(function(["leetcoder","leetcode","od","hamlet","am"]))

def processQueries(queries,m):
    array =  [ i for i in range(1,m+1)]
    res = []
    for q in queries:
        i = array.index(q)
        res.append(i)
        array = [array[i]] + array[:i] + array[i+1:]
    return res
# print (processQueries(queries = [3,1,2,1], m = 5))
# print (processQueries(queries = [4,1,2,2], m = 4))
# print (processQueries(queries = [7,5,5,8,3], m = 8))



def entityParser(text):
    d = {'&quot;':'\"',
         '&apos;':'\'',
         '&amp;':'&',
         '&gt;':'>',
         '&lt;':'<',
         '&frasl;':'/'
         }
    res = []
    i =0
    while i<len(text):
        if text[i] == '&':
            temp = ''
            while i<len(text):
                temp += text[i]
                if text[i] == ';':
                    break
                i += 1
            if temp in d:
                res.append(d[temp])
            else:
                res.append(temp)
            i += 1
            continue
        res.append(text[i])
        i += 1
    return ''.join(res)

# print (entityParser(text = "&amp; is an HTML entity but &ambassador; is not."))
# print (entityParser(text = "and I quote: &quot;...&quot;"))
# print (entityParser(text = "Stay home! Practice on Leetcode :)"))
# print (entityParser(text = "x &gt; y &amp;&amp; x &lt; y is always false"))
# print (entityParser(text = "leetcode.com&frasl;problemset&frasl;all"))




