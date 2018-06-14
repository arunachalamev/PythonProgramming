# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:31:29 2017

@author: arellave
"""

#%%

Denomination = [1,2]
Value = 1

Change = [-1]*(Value+1)

def main():
    print ("Inside main....")
    print ("Denomination = ", Denomination)
    print ("Value    =", Value)
    print ("Change   =", Change)
    print ("Final result=", MinCoinChange(Value),"---")
    

def MinCoinChange(amount):
    print ("----------------")
    print ("Amount value = ", amount)
    if (amount<0): 
        print ("[Inside amount<0]", amount)
        return -1
    
    if (amount ==0 ): 
        print ("[Inside amount == 0]", amount)
        return 0
    
    if (Change[amount]!=-1): 
        print ("Change contains info. amount =", amount, "Change[amount]=", Change[amount])
        return Change[amount]
    
    ans = 0
    for i in range(len(Denomination)):
        print ("Inside for loop i=", i)
        print ("Inside for loop. ans =",ans)
        print ("Inside for loop. Recursion Call =",MinCoinChange(amount- Denomination[i]))
        ans = min (ans,MinCoinChange(amount- Denomination[i]))
        print ("Inside for loop. Updating ans=", ans)
        
    Change[amount] = ans + 1
    print ("Final Change[amount]=", Change[amount])
    return Change[amount]
    

if __name__ == "__main__": main()


#%%