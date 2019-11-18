# There are a row of n houses, each house can be painted with one of the k colors. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix. 
# For example, costs[0][0] is the cost of painting house 0 with color 0; 
# costs[1][2] is the cost of painting house 1 with color 2, and so on... 
# Find the minimum cost to paint all houses.

import math

def paintHouseII(cost):
    numHouse = len(cost)
    if not numHouse:
        return 0
    
    numColors = len(cost[0])
    if not numColors:
        return 0
    
    preMin = 0
    preSecondMin = 0
    preIndex = -1

    for i in range(numHouse):
        curMin = math.inf
        curSecondMin = math.inf
        curIndex = -1
        for j in range(numColors):
            cost[i][j] = cost[i][j] + (preSecondMin if preIndex == j else preMin)

            if cost[i][j] < curMin:
                curSecondMin = curMin
                curMin = cost[i][j]
                curIndex = j
            elif cost[i][j] < curSecondMin:
                curSecondMin = cost[i][j]
        
        preMin= curMin
        preSecondMin = curSecondMin
        preIndex= curIndex
    
    return preMin

print (paintHouseII([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
