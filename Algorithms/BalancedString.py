

def balanced_String(input_string):

    count = 0
    temp = 0

    for x in input_string:
        if x == "R":
            temp = temp + 1
        elif x == "L":
            temp = temp - 1
            
        if temp == 0:
            count = count + 1

    return count




if __name__ == "__main__":
    x = "RLRLLLRRRRRLLL"
    print ('Number of Balanced String {}'.format(balanced_String(x)))