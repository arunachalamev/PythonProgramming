def romanToInt(s):

    my_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    current_value = 0
    prev_value = 0
    sum = 0
    for i in s[::-1]:
        current_value = my_dict[i]
        if current_value < prev_value:
            sum = sum - current_value
        else:
            sum = sum + current_value
        
        prev_value = current_value

    return sum

print (romanToInt("MCMXCIV"))
# print (romanToInt("III"))
