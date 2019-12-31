

def subsets(nums):
    result = [[]]
    for num in nums:
        result += [ [num] +temp for temp in result]
    return result

def subsets1(nums):
    n = len(nums)
    result = []
    bitmask = [bin(x)[3:] for x in range(2**n, 2**(n+1))]
    print (bitmask)
    for bitvalue in bitmask:
        result.append([nums[index] for index,value in enumerate(bitvalue) if bitvalue[index]=='1'])
    return (result)

print (subsets1([1,2,3]))