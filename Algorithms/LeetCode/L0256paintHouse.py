# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
# For example, costs[0][0] is the cost of painting house 0 with color red; 
# costs[1][2] is the cost of painting house 1 with color green, and so on... 
# Find the minimum cost to paint all houses.


def minCost(cost):
    numHouse = len(cost)
    if not numHouse:
        return 0

    for i in range(1,numHouse):
        for j in {0,1,2}:
            cost[i][j] = cost[i][j] + min (cost[i-1][(j+1)%3] , cost[i-1][(j+2)%3] )

    return min (cost[numHouse-1][0], cost[numHouse-1][1], cost[numHouse-1][2])



print(minCost([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))