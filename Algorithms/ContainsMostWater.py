

def contains_more_water(x):
    low_ptr = 0
    high_ptr = len(x) - 1

    max_water = 0

    while (low_ptr < high_ptr):
        height = min (x[low_ptr],x[high_ptr])
        width  = high_ptr - low_ptr

        current_water = width * height

        if (max_water < current_water):
            max_water = current_water
        
        if (x[high_ptr] <= x[low_ptr]):
            high_ptr = high_ptr - 1

        if (x[low_ptr] <= x[high_ptr]):
            low_ptr = low_ptr + 1
    
    return max_water


if __name__ == "__main__":
    x = [1,8,6,2,5,4,8,3,7]
    print (contains_more_water(x))