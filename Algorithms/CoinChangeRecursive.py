# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:06:31 2017

@author: arellave
"""

Denomination = [2,3,4]
Table = [-1]*129

length = len(Denomination)

def MakingChange(n):
   # global Table, Denomination, length
    if (n<0):
        return -1
    
    if(n==0):
        return 0
    
    if (Table[n] != -1):
        return Table[n]
        
    ans = -1
    for i in range(length):
        print "i,n, n- D[i], MakingChange(n-D[i]): ->",i, n, n-Denomination[i], MakingChange(n-Denomination[i])
        ans = min (ans,MakingChange(n-Denomination[i]) )
    
    Table[n] = ans +1
    return Table[n]
        




if __name__ == "__main__": 
    print "Main:" ,MakingChange(5)
    