# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 +bx + c to each element x in the array.
# The returned array must be in sorted order.
# Expected time complexity: O(n)
# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
# Result: [3, 9, 15, 33]
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
# Result: [-23, -5, 1, 7]

def sortTransformedArray(nums,a,b,c):
    start, end = 0, len(nums)-1
    result = [0]* len(nums)
    i,j = start, end
    while (start<=end):
        first = calculate(nums[start],a,b,c)
        second = calculate(nums[end],a,b,c)
        if a>=0:
            if first > second:
                result[j] = first
                j = j - 1
                start = start + 1
            else:
                result[j] = second
                j = j - 1
                end = end -1
        else:
            if first > second:
                result[i] = second
                i = i + 1
                end = end -1
            else:
                result[i] = first
                i = i + 1
                start = start+ 1

    return result

def calculate (x,a,b,c):
    return a*x*x + b*x + c

print (sortTransformedArray([-4,-2,2,4],1,3,5))
print (sortTransformedArray([-4,-2,2,4],-1,3,5))