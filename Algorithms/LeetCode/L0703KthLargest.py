import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        #print (self.nums) #[2,4,8,5]
        while(len(self.nums)>k):
            heapq.heappop(self.nums)
        #print (self.nums) #[4,5,8]

        

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]

        

k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
print(kthLargest.add(3))  #returns 4
print(kthLargest.add(5))  #returns 5
print(kthLargest.add(10)) #returns 5
print(kthLargest.add(9))   #returns 8
print(kthLargest.add(4))   #returns 8
