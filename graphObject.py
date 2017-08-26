# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:50:46 2017

@author: arellave
"""

import networkx as nx
from random import random

N = 1000

G = nx.Graph()
for i in range(N):
    for j in range(N):
        G.add_edge(i,j,weight= random())

T=nx.minimum_spanning_tree(G)
edges = T.edges(data=True)

print (sum([e[2]["weight"] for e in edges]))
