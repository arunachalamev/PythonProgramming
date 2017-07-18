# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:40:24 2017

@author: arellave
"""

coins = [1,2,6]

def MinimumCoinChange(V):
#    raw_input()
    if V<=0: 
        return 0
    res = float("inf")
    for i in range(len(coins)):
        sub_residual = MinimumCoinChange(V-coins[i])
        if (sub_residual != float("inf") and (sub_residual+1) < res):
            res = sub_residual + 1
    return res


def min_change(V, C):
    m, n = len(V)+1, C+1
    table = [[0] * n for x in xrange(m)]
    for j in xrange(1, n):
        table[0][j] = float('inf')
    for i in xrange(1, m):
        for j in xrange(1, n):
            aC = table[i][j - V[i-1]] if j - V[i-1] >= 0 else float('inf')
            table[i][j] = min(table[i-1][j], 1 + aC)
    return table[m-1][n-1]
    
    
if __name__ == "__main__":
    print min_change([1,2,3],10)    