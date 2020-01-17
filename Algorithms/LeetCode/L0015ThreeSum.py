

def threeSum(nums):
    nums = sorted(nums)
    result = set()
    temp = []
    for i in range(len(nums)-2):
        if nums[i]>0: break

        l, r = i+1, len(nums) -1

        while(l<r):
            total = nums[i] + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else: 
                result.add((nums[i],nums[l],nums[r]))
                r = r-1
                l = l+1
        
    for x in result:
        temp.append(list(x))
    return temp

print (threeSum([-1, 0, 1, 2, -1, -4]))
