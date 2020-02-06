

def numFriendRequests(ages):
    count = [0]*121
    for age in ages:
        count[age] += 1

    result = 0
    for ageA,countA in enumerate(count):
        for ageB,countB in enumerate(count):
            if ageB <= 0.5* ageA + 7: continue
            if ageB > ageA : continue
            if ageB > 100 and ageA <100: continue
            result = result + countA * countB
            if ageA == ageB : result = result - countA
    
    return result


print (numFriendRequests([16,16]))
