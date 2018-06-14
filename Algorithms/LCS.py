# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:24:49 2017

@author: arellave
"""

#%%

FS = "ABC"
SS = "2222A"

lenFS = len(FS)
lenSS = len(SS)

LCS = [[0 for j in range(lenSS+1)] for i in range(lenFS+1)]

print (LCS)

for i in range(lenFS-1,-1,-1):
    for j in range(lenSS-1,-1,-1):
        LCS[i][j] = LCS[i+1][j+1]
        if (FS[i]==SS[j]):
            LCS[i][j] =  LCS[i][j] +1
        else:
            LCS[i][j] = max(LCS[i][j],LCS[i+1][j],LCS[i][j+1])

print (LCS)
print (LCS[0][0])
                

#%%