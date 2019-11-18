# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
# write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, 
# you could climb any number from a set of positive integers X? 
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def numberOfSteps(n):
    F = [0]*(n+1)
    F[0]= 1
    F[1]= 1

    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    
    return F[-1]


def numberOfSteps2(n,stepSizes):
    result = list()

    for step in stepSizes:
        if n == step:
            result.append([step])
        elif n > step:
            combinations = numberOfSteps2(n-step,stepSizes)
            for c in combinations:
                result.append([step] + c)
    return result


print (numberOfSteps(4))
print (numberOfSteps2(4,[1,2]))
