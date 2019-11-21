# Houese and heater
# find the min radius to cover houses 

# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, 
# then all the houses can be warmed

def findRadius(houses,heaters):
    houses.sort()
    heaters.sort()

    heaters = [float('-inf')] + heaters + [float('inf')]
    i,dis,ans = 0,0,0
    for house in houses:
        while house > heaters[i]:
            i = i + 1
        dis = min(house-heaters[i-1], heaters[i]-house)
        ans = max(ans,dis)
    return ans

print (findRadius([1,2,3,4],[1,4]))