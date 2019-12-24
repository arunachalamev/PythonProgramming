

def mySqrt(x):
    if x<2: return x
    low, high = 2, x//2
    while low<=high:
        mid = low + (high-low)//2
        if mid*mid > x:
            high = mid -1
        elif mid * mid < x:
            low = mid +1
        else:
            return mid
    return high


print (mySqrt(80))