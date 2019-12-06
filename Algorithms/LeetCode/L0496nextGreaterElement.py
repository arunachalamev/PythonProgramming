

def nextGreaterElement(nums1, nums2):
    result = []
    for x in nums1:
        flag, count  = 0, 0
        for y in nums2:
            if x == y:
                flag = 1
                count = count + 1
                continue
            if flag == 1 and y > x:
                result.append(y)
                break
            count = count + 1
        if count == len(nums2):
            result.append(-1)
    return result

print (nextGreaterElement([4,1,2],[1,3,4,2]))
print (nextGreaterElement([2,4],[1,2,3,4]))

            
