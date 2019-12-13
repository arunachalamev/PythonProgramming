
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() 
# that returns an integer from 1 to 7 (inclusive).

import random

def rand7():
    val = [[1,2,3,4,5],
            [6,7,1,2,3],
            [4,5,6,7,1],
            [2,3,4,5,6],
            [7,0,0,0,0]
            ]
    
    value = 0

    while (value ==0):
        i = random.randrange(1,5)
        j = random.randrange(1,5)

        value = val[i-1][j-1]

    return value

print (rand7())


def rand7_2():
    i = 5*random.randint(1,5) + random.randint(1,5) - 5
    if i <21:
        return i%7 + 1
    return rand7_2()


print (rand7_2())
