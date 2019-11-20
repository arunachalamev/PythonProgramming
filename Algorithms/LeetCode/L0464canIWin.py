# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. 
# The player who first causes the running total to reach or exceed 100 wins.
# What if we change the game so that players cannot re-use integers?
# For example, two players might take turns drawing from a common pool of numbers of 1..15 
# without replacement until they reach a total >= 100.
# Given an integer maxChoosableInteger and another integer desiredTotal, 
# determine if the first player to move can force a win, assuming both players play optimally.
# You can always assume that maxChoosableInteger will not be larger than 20 
# and desiredTotal will not be larger than 300.


def canIWin(maxChoosableInteger,desiredTotal):
    if (1+maxChoosableInteger) * maxChoosableInteger /2 < desiredTotal:
        return False
    
    tempArray = {}

    def helper (nums, desiredTotal):
        hash = str(nums)
        if hash in tempArray:
            return tempArray[hash]
        
        if nums[-1] > desiredTotal:
            return True

        for i in range(len(nums)):
            if not helper(list(nums[:i]) + list(nums[i+1:]),desiredTotal- nums[i]):
                tempArray[hash] = True
        
        tempArray[hash] = False
        return False

    return helper(range(1,maxChoosableInteger+1),desiredTotal)



print(canIWin(10,11))
