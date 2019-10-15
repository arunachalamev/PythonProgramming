#RunningTime : O(n)
#Space : No additional memory

def missing_number(x):

    for i in range(len(x)):
        new_index = abs(x[i])-1

        if x[new_index] > 0:
            x[new_index] *= -1
    
    result = []
    for i in range(1,len(x)+1):
        if x[i-1] > 0:
            result.append(i)
    
    return result





if __name__ == "__main__":
    x = [4,3,2,7,8,2,3,1]
    print(missing_number(x))
