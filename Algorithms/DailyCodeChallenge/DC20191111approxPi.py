import random
import math

def approximatePi():

    numOfPoints = 0
    insideCircle = 0

    for i in range(10000):
        numOfPoints = numOfPoints + 1

        x = random.random()
        y = random.random()

        if math.sqrt(x**2 + y**2) <= 1:
            insideCircle = insideCircle + 1

    return 4*insideCircle/numOfPoints


def approximatePi2(numOfTrials):
    inside = 0
    r = 2
    for i in range(numOfTrials):
        x = random.random()*r
        y = random.random()*r

        if x**2 + y**2 <= r**2:
            inside = inside + 1

    return round(4*inside/numOfTrials,3)


print(approximatePi())
print(approximatePi2(10000))


