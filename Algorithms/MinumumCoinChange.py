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

if __name__ == "__main__":
    print MinimumCoinChange(15)
