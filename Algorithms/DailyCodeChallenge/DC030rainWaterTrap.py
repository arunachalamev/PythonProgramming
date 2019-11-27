
# calculate the trapped rain water

def rainWaterTrap(height):
    i, j = 0, len(height) -1
    result, leftMax, rightMax = 0, 0, 0
    while (i<=j):
        leftMax = max(leftMax,height[i])
        rightMax = max(rightMax,height[j])

        if  (leftMax<rightMax):
            result = result + (leftMax - height[i])
            i = i + 1
        else:
            result = result + (rightMax - height[j])
            j = j - 1

    return result


print (rainWaterTrap([2,1,2])) # 2
print (rainWaterTrap([3,0,1,3,0,5])) #8
print (rainWaterTrap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
