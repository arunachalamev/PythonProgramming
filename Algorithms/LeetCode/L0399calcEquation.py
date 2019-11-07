
# Equations are given in the format A / B = k, where A and B are variables represented as strings, 
# and k is a real number (floating point number). Given some queries, return the answers. 
# If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].


#Floyd - Warshall Algorithm
import collections
import itertools

def calcEquation(equations,values,queries):
    quot = collections.defaultdict(dict)

    for (num, den),val in zip(equations,values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1/ val

#    for k, i, j in itertools.permutations(quot, 3):
#         if k in quot[i] and j in quot[k]:
#             quot[i][j] = quot[i][k] * quot[k][j]
    
    for k in quot:
        for i in quot[k]:
            for j in quot[k]:
                quot[i][j]= quot[i][k] * quot[k][j]
    
    result = [quot[num].get(den,-1.0) for num,den in queries]

    return result


#Using DFS
def calcEquation2(equations,values,queries):
    graph = {}

    def build_graph(equations,value):
        def add_edge(f,t,value):
            if f in graph:
                graph[f].append((t,value))
            else:
                graph[f] = [(t,value)]

        for vertice,value in zip(equations,values):
            f,t = vertice
            add_edge(f,t,value)
            add_edge(t,f,1/value)

    def find_path(query):
        b,e = query
        if b not in graph or e not in graph:
            return -1.0
        
        q = collections.deque([(b,1.0)])
        visited = set()

        while q:
            front, cur_product = q.popleft()
            if front == e:
                return cur_product
            visited.add(front)
            for neighbor, value in graph[front]:
                if neighbor not in visited:
                    q.append((neighbor,cur_product*value))
        
        return -1.0

    build_graph(equations,values)
    return [find_path(q) for q in queries]



equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]


print(calcEquation(equations,values,queries))
print(calcEquation2(equations,values,queries))

