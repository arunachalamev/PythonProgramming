import collections

def isPossibleDivide(nums, k):
    if len(nums) == 0 and k ==0: return True
    if len(nums) == 0 and k!=0: return False
    if len(nums)%k !=0: return False

    counter =0

    s = collections.Counter(nums)
    while (counter < len(nums)):
        minX = min(x for x,y in s.items() if y!=0)
        # print (minX)
        for i in range(minX,minX+k):
            s[i] -= 1
            counter +=1

    # print (s)
    if max(y for x,y in s.items()) != 0:
        return False
    return True
    
print (isPossibleDivide([1,2,3,3,4,4,5,6],4))
print (isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11],3))
print (isPossibleDivide([3,3,2,2,1,1],3))
print (isPossibleDivide([1,2,3,4],3))
