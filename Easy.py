def twoSum(nums,target):
    d = {}
    for i,x in enumerate(nums):
        if (target-x) in d:
            return d[target-x], i
        d[x] = i
    return -1
# print (twoSum([2,7,11,15],9))

def reverse(x):
    sign = [1,-1][x<0]
    rev, x = 0, abs(x)
    while x:
        x, mod = divmod(x,10)
        rev = rev*10 + mod
    return rev*sign if -pow(2,31)<= rev*sign <= pow(2,31)-1 else 0
# print (reverse(123))
# print (reverse(-123))
# print (reverse(120))

def isPalindrome(x):
    if x<0 or (x%10 ==0 and x!=0):
        return False
    rev = 0
    while x > rev:
        x, mod = divmod(x,10)
        rev = rev*10 + mod
    return x == rev or x == rev//10
# print (isPalindrome(121))
# print (isPalindrome(-121))
# print (isPalindrome(10))

def romanToInt(s):
    d = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            z -= d[s[i]]
        else:
            z += d[s[i]]
    return z+d[s[-1]]
# print (romanToInt('LVIII'))
# print (romanToInt('IX'))
# print (romanToInt('MCMXCIV'))

def longestCommonPrefix(strs):
    if not strs: return ""
    minstr = min(strs,key = len)
    for i, ch in enumerate(minstr):
        for others in strs:
            if others[i] != ch:
                return minstr[:i]
    return minstr
# print (longestCommonPrefix(["flower","flow","flight"]))

def isValid(s):
    d = {']':'[',')':'(','}':'{'}
    stack = []
    for x in s:
        if x in d:
            top = stack.pop() if stack else '#'
            if top != d[x]:
                return False
        else:
            stack.append(x)
    return not stack
# print (isValid('(((((())))))'))
# print (isValid('()[]{}'))
# print (isValid('([)]'))

class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1,l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1,l2.next)
        return l2

def mergeTwoListsIterative(l1,l2):
    prehead = ListNode(-1)
    prev = prehead
    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next    
    prev.next = l1 if l1 is not None else l2
    return prehead.next
# l1 = ListNode(1, ListNode(2, ListNode(4)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
# print (mergeTwoLists(l1,l2))

def removeDuplicates(nums):
    l,r = 0, 1
    while r<len(nums):
        if nums[l] == nums[r]:
            r += 1
        else:
            l += 1
            nums[l] = nums[r]
            r += 1
    return l+1
# print (removeDuplicates([1,1,2]))
# print (removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

def strStr(haystack, needle):
    h,n = len(haystack), len(needle)
    for i in range(h-n+1):
        if haystack[i:i+n] == needle:
            return i
    return -1

def strStr2(haystack,needle):
    h,n = len(haystack), len(needle)
    if n==0: 
        return 0
    ph = 0
    while ph < h-n+1:
        while ph < h-n+1 and haystack[ph] != needle[0]:
            ph += 1
        curr_len = pn = 0
        while pn < n and ph < h and haystack[ph] == needle[pn]:
            pn += 1
            ph += 1
            curr_len += 1
        if curr_len == n:
            return ph-n
    return -1

def strStr3(haystack,needle):
    L,n = len(needle), len(haystack)
    if L> n: return -1

    a, modulus = 26, 2**31

    h_to_int = lambda i: ord(haystack[i]) - ord('a')
    needle_to_int = lambda i: ord(needle[i]) - ord('a')

    h = ref_h = 0
    for i in range(L):
        h = ( h*a + h_to_int(i) ) % modulus
        ref_h = ( ref_h*a + needle_to_int(i) ) % modulus
    if h == ref_h:
        return 0
    
    aL = pow(a,L,modulus)
    for start in range(1,n-L+1):
        h = h*a - h_to_int(start-1)*aL + h_to_int(start+L-1)% modulus
        if h == ref_h:
            return start
    return -1
# print (strStr3('leetcode','de'))



# does not work for negative number
def maxSubArray(nums):
    max_so_far = max_ending_here = 0
    for x in nums:
        max_ending_here += x
        if max_ending_here < 0:
            max_ending_here =0
        max_so_far = max (max_so_far, max_ending_here)
    return max_so_far

def maxSubArray2 (nums):
    current_max= max_so_far = nums[0]
    for i in range(1,len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(current_max, max_so_far)
    return max_so_far

def maxSubArray3(nums):
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        max_so_far = max(max_so_far, nums[i])
    return max_so_far
# divide and conqure strategy exist
# print (maxSubArray3([-2,1,-3,4,-1,2,1,-5,4]))


def plusOne(digits):
    n = len(digits)
    for i in range(n):
        idx = n-i-1
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits
    return [1] + digits
# print (plusOne([9,9,9]))

def plusOneLinkedList(head):
    sentinel = ListNode(0)
    sentinel.next = head
    not_nine = sentinel

    while head:
        if head.val !=9:
            not_nine = head
        head = head.next
    
    not_nine.val += 1
    not_nine = not_nine.next

    while not_nine:
        not_nine.val = 0
        not_nine = not_nine.next
    
    return sentinel if sentinel.val else sentinel.next
# print (plusOneLinkedList(ListNode(1,ListNode(2, ListNode(3)))))


def addBinary(a,b):
    x,y = int(a,2), int(b,2)
    while y:
        ans = x^y
        carry = (x & y)<<1
        x,y = ans, carry
    return bin(x)[2:]
# print (addBinary('11','10'))

def addBinary2(a,b):
    n = max(len(a),len(b))
    a,b = a.zfill(n), b.zfill(n)

    carry, ans = 0 , []
    for i in range(n-1,-1,-1):
        if a[i] == '1': carry += 1
        if b[i] == '1': carry += 1

        if carry %2 == 1: ans.append('1')
        else: ans.append('0')

        carry //= 2
    
    if carry == 1: ans.append('1')
    ans.reverse()

    return ''.join(ans)
# print (addBinary2('11','10'))

def mySqrt(x):
    if x<2: return x
    low ,high = 2, x//2
    while low <= high:
        mid = low + (high - low)//2
        if mid * mid > x:
            high = mid -1
        elif mid * mid < x:
            low = mid + 1
        else:
            return mid
    return high
# print (mySqrt(9))

def climbStairs(n):
    def climb(i,n):
        if i > n: return 0
        if i == n: return 1
        return climb(i+1,n) + climb(i+2,n)
    return climb (0,n)

def climbStairs2(n):
    if n==1: return 1
    dp =[0]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]
# print (climbStairs2(6))

def merge(num1,m,num2,n):
    p1, p2 = m-1, n-1
    p = m+n-1
    while p1>=0 and p2>=0:
        if num1[p1] < num2[p2]:
            num1[p] = num2[p2]
            p2 -= 1
        else:
            num1[p] = num1[p1]
            p1 -= 1
        p -= 1
    num1[:p2+1] = num2[:p2+1]
    return num1
# print (merge([1,2,3,0,0,0],3,[2,5,6],3))

class TreeNode:
    def __init__ (self,val,left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

import collections
def isSameTreeIterative(p,q):
    queue = collections.deque()
    queue.append((p,q))
    while queue:
        x,y = queue.popleft()
        if not x and not x:
            continue
        if not x or not y:
            return False
        if x.val != y.val:
            return False
        queue.append((x.left,y.left))
        queue.append((x.right,y.right))
    return True

# print (isSameTreeIterative(TreeNode(1,TreeNode(2),TreeNode(3)),TreeNode(1,TreeNode(2),TreeNode(3))))
# print (isSameTreeIterative(TreeNode(1,TreeNode(2),None),TreeNode(1,None,TreeNode(2))))


def isSymmetric(root):
    def isMirror(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and isMirror(p.left,q.right) and isMirror(p.right,q.left)
    return isMirror(root,root)
# print(isSymmetric(TreeNode(1,TreeNode(2),TreeNode(3))))

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

def maxDepthIterative(root):
    stack = []
    if root is not None:
        stack.append((1,root))
    depth = 0
    while stack:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append(current_depth+1, root.left)
            stack.append(current_depth+1, root.right)
    return depth
# print (maxDepth(TreeNode(1,TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7)))))

def sortedArrayToBST(nums):
    def helper(array, lo, hi):
        if lo > hi:
            return None
        mid = (lo +hi) //2
        x = TreeNode(nums[mid])
        x.left = helper(array, lo, mid-1)
        x.right = helper(array, mid+1, hi)
        return x

    return helper(nums, 0, len(nums)-1)
# print (sortedArrayToBST([-10,-3,0,5,9]))

def isBalanced(root):
    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))

    if root:
        L = height(root.left)
        R = height(root.right)
        return abs(L-R)<2 and isBalanced(root.left) and isBalanced(root.right)
    else:
        return True
# print (isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
# print (isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))

def minDepth(root):
    if root is None:
        return 0
    stack , ans = [(root,1)], float('inf')
    while stack:
        node,depth = stack.pop()
        if node.left is None and node.right is None:
            ans = min (ans, depth)
        if node.left : stack.append((node.left, depth + 1))
        if node.right : stack.append((node.right, depth + 1))
    return ans
# print (minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

def hasPathSum(root,sum):
    if root is None:
        return 0
    stack = [(root, root.val)]
    while stack:
        node, total = stack.pop()
        if total == sum and node.left is None and node.right is None:
            return True
        if node.left: stack.append((node.left, total + node.left.val))
        if node.right: stack.append((node.right, total + node.right.val))
    return False
# print (hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))),22))

def generate(num_rows):
    triange = []
    for i in range(num_rows):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1,1
        for j in range(1,len(row)-1):
            row[j] = triange[i-1][j-1] + triange[i-1][j]
        triange.append(row)
    return triange
# print (generate(5))

def maxProfit(prices):
    minBuying, maxProfit = prices[0], 0
    for i in range(1, len(prices)):
        if prices[i] < minBuying:
            minBuying = prices[i]
        if maxProfit < (prices[i] - minBuying):
            maxProfit = prices[i] - minBuying
    return maxProfit
# print (maxProfit([7,6,4,3,1]))

def maxProfitII(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i-1] < prices [i]:
            profit += prices[i] - prices[i-1]
    return profit 
# print (maxProfitII([7,6,4,3,1]))

def isPalindromeSentence(s):
    if len(s) == 0 : return True
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    i, j = 0, len(s)-1
    while (i<j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
# print (isPalindromeSentence("A man, a plan, a canal: Panama"))

def singleNumer(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans
# print (singleNumer([4,1,2,1,2]))

def hasCycle(head):
    if head is None or head.next is None:
        return False
    slow, fast = head, head.next
    while (slow != fast):
        if fast is None or fast.Next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None
    pA, pB = headA, headB
    while pA is not pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    return pA

def twoSumAscending(nums,target):
    i, j = 0, len(nums)-1
    while i<j:
        temp = nums[i] + nums[j]
        if temp < target: i += 1
        elif temp > target: j -= 1
        else: return (i+1,j+1)
    return None
# print (twoSumAscending([2,7,11,15],9))

def convertToTitle(n):
    temp = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
    result = []
    if n<26: return temp[n%26]
    while n>1:
        rem, n  = n % 26, n // 26
        result.append(temp[rem])
    return ''.join(result[::-1])
# print (convertToTitle(26))


def P189_rotate(nums,k):
    def _reverse(array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start, end = start + 1, end - 1
    if k <= 0: return nums
    k, n = k % len(nums) , len(nums) - 1
    _reverse(nums, 0, n-k)
    _reverse(nums, n-k+1, n)
    _reverse(nums, 0, n)
    return nums
# print (P189_rotate([1,2,3,4,5,6,7],3))

def P191_hammingWeight(n):
    c =0
    while n: 
        n = n & (n-1)
        c += 1
    return c
def P191_hammingWeightRecursive(n,count):
    if n == 0:
        return count
    else:
        return P191_hammingWeightRecursive(n & n-1,count+1)
# print (P191_hammingWeightRecursive(5,0))

def P202_isHappy(n):
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n,10)
            total_sum += digit ** 2
        return total_sum
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n==1
# print (P202_isHappy(19))

def P206_reverseListIterative(head):
    prev, curr = None, head
    while curr != None:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev
def P206_reverseListRecursive(head):
    if head is None or head.next is None: return head
    p = P206_reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return p

def P226_invertTree(root):
    if root is None:
        return
    else:
        left, right = P226_invertTree(root.left), P226_invertTree(root.right)
        root.left, root.right = right, left
        return root



