# You have a pointer at index 0 in an array of size arrLen. 
# At each step, you can move 1 position to the left, 1 position to the right in the array 
# or stay in the same place  (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer 
# still at index 0 after exactly steps steps.

# Since the answer may be too large, return it modulo 10^9 + 7.

def numWays(steps, n):
    MOD = 10**9 + 7
    # @lru_cache(none)
    def calculate(pos,steps):
        if pos<0 or pos>=n : return 0
        if pos > steps: return 0
        if steps == pos: return 1
        steps -= 1
        return (calculate(pos+1,steps) + calculate(pos-1, steps) + calculate(pos,steps))%MOD
    
    return calculate(0,steps)

print (numWays(3,2))
print (numWays(2,4))
print (numWays(4,2))
