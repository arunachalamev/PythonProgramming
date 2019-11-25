# Input: 4, 14, 2
# Output: 6
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

# reason: count('0')*count('1') at i-th bit position and sum for all bit position

def totalHammingDistance(nums):
    if not len(nums): return 0
    
    bit = [[0,0] for _ in range(32)]
    
    for x in nums:
        for i in range(32):
            bit[i][x%2] += 1
            x = int(x/2)
    
    return sum(x*y for x,y in bit)


print (totalHammingDistance([4,14,2]))