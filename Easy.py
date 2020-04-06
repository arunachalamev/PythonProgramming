def P1_twoSum(nums,target):
    d = {}
    for i,x in enumerate(nums):
        if (target-x) in d:
            return d[target-x], i
        d[x] = i
    return -1
# print (P1_twoSum([2,7,11,15],9))

def P7_reverse(x):
    sign = [1,-1][x<0]
    rev, x = 0, abs(x)
    while x:
        x, mod = divmod(x,10)
        rev = rev*10 + mod
    return rev*sign if -pow(2,31)<= rev*sign <= pow(2,31)-1 else 0
# print (P7_reverse(123))
# print (P7_reverse(-123))
# print (P7_reverse(120))

def P9_isPalindrome(x):
    if x<0 or (x%10 ==0 and x!=0):
        return False
    rev = 0
    while x > rev:
        x, mod = divmod(x,10)
        rev = rev*10 + mod
    return x == rev or x == rev//10
# print (P9_isPalindrome(121))
# print (P9_isPalindrome(-121))
# print (P9_isPalindrome(10))

def P13_romanToInt(s):
    d = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            z -= d[s[i]]
        else:
            z += d[s[i]]
    return z+d[s[-1]]
# print (P13_romanToInt('LVIII'))
# print (P13_romanToInt('IX'))
# print (P13_romanToInt('MCMXCIV'))

def P14_longestCommonPrefix(strs):
    if not strs: return ""
    minstr = min(strs,key = len)
    for i, ch in enumerate(minstr):
        for others in strs:
            if others[i] != ch:
                return minstr[:i]
    return minstr
# print (P14_longestCommonPrefix(["flower","flow","flight"]))

def P20_isValid(s):
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
# print (P20_isValid('(((((())))))'))
# print (P20_isValid('()[]{}'))
# print (P20_isValid('([)]'))

class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
def P21_mergeTwoLists(l1,l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = P21_mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = P21_mergeTwoLists(l1,l2.next)
        return l2

def P21_mergeTwoListsIterative(l1,l2):
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
# print (P21_mergeTwoListsIterative(l1,l2))

def P26_removeDuplicates(nums):
    l,r = 0, 1
    while r<len(nums):
        if nums[l] == nums[r]:
            r += 1
        else:
            l += 1
            nums[l] = nums[r]
            r += 1
    return l+1
# print (P26_removeDuplicates([1,1,2]))
# print (P26_removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

def P28_strStr(haystack, needle):
    h,n = len(haystack), len(needle)
    for i in range(h-n+1):
        if haystack[i:i+n] == needle:
            return i
    return -1

def P28_strStr2(haystack,needle):
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

def P28_strStr3(haystack,needle):
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
def P53_maxSubArray(nums):
    max_so_far = max_ending_here = 0
    for x in nums:
        max_ending_here += x
        if max_ending_here < 0:
            max_ending_here =0
        max_so_far = max (max_so_far, max_ending_here)
    return max_so_far

def P53_maxSubArray2 (nums):
    current_max= max_so_far = nums[0]
    for i in range(1,len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(current_max, max_so_far)
    return max_so_far

def P53_maxSubArray3(nums):
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        max_so_far = max(max_so_far, nums[i])
    return max_so_far
# divide and conqure strategy exist
# print (maxSubArray3([-2,1,-3,4,-1,2,1,-5,4]))


def P66_plusOne(digits):
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

def P66_plusOneLinkedList(head):
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


def P67_addBinary(a,b):
    x,y = int(a,2), int(b,2)
    while y:
        ans = x^y
        carry = (x & y)<<1
        x,y = ans, carry
    return bin(x)[2:]
# print (addBinary('11','10'))

def P67_addBinary2(a,b):
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

def P69_mySqrt(x):
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

def P70_climbStairs(n):
    def climb(i,n):
        if i > n: return 0
        if i == n: return 1
        return climb(i+1,n) + climb(i+2,n)
    return climb (0,n)

def P70_climbStairs2(n):
    if n==1: return 1
    dp =[0]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]
# print (climbStairs2(6))

def P88_merge(num1,m,num2,n):
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

def P100_isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and P100_isSameTree(p.left,q.left) and P100_isSameTree(p.right,q.right)

import collections
def P100_isSameTreeIterative(p,q):
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


def P101_isSymmetric(root):
    def isMirror(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and isMirror(p.left,q.right) and isMirror(p.right,q.left)
    return isMirror(root,root)
# print(isSymmetric(TreeNode(1,TreeNode(2),TreeNode(3))))

def P104_maxDepth(root):
    if root is None:
        return 0
    return 1 + max(P104_maxDepth(root.left),P104_maxDepth(root.right))

def P104_maxDepthIterative(root):
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

def P108_sortedArrayToBST(nums):
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

def P110_isBalanced(root):
    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))

    if root:
        L = height(root.left)
        R = height(root.right)
        return abs(L-R)<2 and P110_isBalanced(root.left) and P110_isBalanced(root.right)
    else:
        return True
# print (isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
# print (isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))

def P111_minDepth(root):
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

def P112_hasPathSum(root,sum):
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

def P118_generate(num_rows):
    triange = []
    for i in range(num_rows):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1,1
        for j in range(1,len(row)-1):
            row[j] = triange[i-1][j-1] + triange[i-1][j]
        triange.append(row)
    return triange
# print (generate(5))

def P121_maxProfit(prices):
    minBuying, maxProfit = prices[0], 0
    for i in range(1, len(prices)):
        if prices[i] < minBuying:
            minBuying = prices[i]
        if maxProfit < (prices[i] - minBuying):
            maxProfit = prices[i] - minBuying
    return maxProfit
# print (maxProfit([7,6,4,3,1]))

def P122_maxProfitII(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i-1] < prices [i]:
            profit += prices[i] - prices[i-1]
    return profit 
# print (maxProfitII([7,6,4,3,1]))

def P125_isPalindromeSentence(s):
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

def P136_singleNumer(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans
# print (singleNumer([4,1,2,1,2]))

def P141_hasCycle(head):
    if head is None or head.next is None:
        return False
    slow, fast = head, head.next
    while (slow != fast):
        if fast is None or fast.Next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

def P160_getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None
    pA, pB = headA, headB
    while pA is not pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    return pA

def P167_twoSumAscending(nums,target):
    i, j = 0, len(nums)-1
    while i<j:
        temp = nums[i] + nums[j]
        if temp < target: i += 1
        elif temp > target: j -= 1
        else: return (i+1,j+1)
    return None
# print (twoSumAscending([2,7,11,15],9))

def P168_convertToTitle(n):
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
# print (P191_hammingWeight(7))

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

def P235_lowestCommonAncestor(root,p,q):
    if root.val < p.val and root.val < q.val:
        return P235_lowestCommonAncestor(root.right,p,q)
    elif root.val > p.val and root.val > q.val:
        return P235_lowestCommonAncestor(root.left,p,q)
    else:
        return root

def P242_isAnagram(s,t):
    if len(s) != len(t) : return False
    s, t = sorted(s), sorted(t)
    for x,y in zip(s,t):
        if x != y : return False
    return True
# print (P242_isAnagram('anagram','nagaram'))

def P246_isStrobogrammatic(nums):
    d = {('0','0'),('1','1'),('6','9'),('8','8')}
    i,j = 0, len(nums)-1
    while i<= j:
        if (nums[i],nums[j]) not in d:
            return False
        i, j = i+1, j-1
    return True
# print (P246_isStrobogrammatic('962'))

def P252_canAttendMeetings(intervals):
    intervals = sorted(intervals)
    prevE = 0
    for x,y in intervals:
        if x < prevE:
            return False
        prevE = y
    return True
# print (P252_canAttendMeetings([[7,10],[2,4]]))

def P257_binaryTreePaths(root):
    if root is None: return []
    paths = []
    stack = [(root,str(root.val))]
    while stack:
        node, path = stack.pop()
        if node.left is None and node.right is None:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.val)))
    return paths
# print (P257_binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)),TreeNode(3))))

def P266_canPermutePalindrome(s):
    temp = set()
    for ch in s:
        if ch in temp:
            temp.remove(ch)
        else:
            temp.add(ch)
    return len(temp) <= 1
# print (P266_canPermutePalindrome('aab'))

def P268_missingNumber(nums):
    return (len(nums)*(len(nums)+1)//2) - sum(nums)
# print (P268_missingNumber([9,6,4,2,3,5,7,0,1]))

def P270_closetValue(root, target):
    def inorder(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    return min(inorder(root), key=lambda x: abs(x-target))
# print (P270_closetValue(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),TreeNode(5)),3.7))

def P278_firstBadVersion(n):
    left, right = 1, n
    while (left <= right):
        mid = left + (right-left)//2
        if mid : # Actual code: isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

def P283_moveZeros(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] !=0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    print(nums)
# print (P283_moveZeros([1,0,1]))

def P303_sumRange(nums,i,j):
    prefixSum = [0]*(len(nums)+1)
    for index,x in enumerate(nums):
        prefixSum[index+1] = prefixSum[index] + x
    return prefixSum[j+1]-prefixSum[i]
# print (P303_sumRange([-2, 0, 3, -5, 2, -1],0,2))

def P339_depthSum(nestedList):
    depth, res = 1, 0
    while nestedList:
        res += sum([x.getInteger() for x in nestedList if x.isInteger()])
        nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
        depth += 1
    return res
# input: [[1,1],2,[1,1]]

def P344_reverseString(s):
    i,j = 0, len(s)-1
    while (i<j):
        s[i], s[j] = s[j], s[i]
        i, j = i+1, j-1
    print (s)
# print (P344_reverseString(["h","e","l","l","o"]))


def P349_intersection(nums1, nums2):
    def set_intersection(set1, set2):
        return [x for x in set1 if x in set2]
    set1, set2 = set(nums1), set(nums2)
    if len(set1) < len(set2):
        return set_intersection(set1,set2)
    else:
        return set_intersection(set2,set1)
# print(P349_intersection([1,2,2,1],[2,2]))


def P350_intersect(nums1,nums2):
    counts = collections.Counter(nums1)
    res =[]
    for x in nums2:
        if counts[x] > 0:
            res.append(x)
            counts[x] -= 1
    return res
# print(P350_intersect([1,2,2,1],[2,2]))

def P371_getSumIterative(a,b):
    while (b !=0):
        c = a & b
        a = a ^ b
        b = c << 1
    return a
def P371_getSumRecursive(a,b):
    if b ==0:
        return a
    return P371_getSumRecursive(a^b, (a&b) << 1)
# print (P371_getSumRecursive(2,3))

def P387_firstUniqChar(s):
    count = collections.Counter(s)
    for i,ch in enumerate(s):
        if count[ch] == 1: 
            return i
    return -1
# print (P387_firstUniqChar('loveleetcode'))

def P392_isSubsequence(s,t):
    i = 0
    for ch in t:
        if ch == s[i]:
            i += 1
            if i >= len(s):
                return True
    return False
# print(P392_isSubsequence('axc','ahbgdc'))
# Follow up question

def P404_sumOfLeftLeaves(root):
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + P404_sumOfLeftLeaves(root.right)
    return P404_sumOfLeftLeaves(root.left) + P404_sumOfLeftLeaves(root.right)

def P405_toHex(num):
    if num == 0: return '0'
    map = '0123456789abcdef'
    ans = ''
    for _ in range(8): #for 32 bits
        rem = num & 15
        ans = map[rem] + ans
        num = num >> 4
    return ans.lstrip('0')
# print (P405_toHex(-1))

def P408_validWordAbbrevation(word,abbr):
    i = j = 0
    m, n = len(word), len(abbr)
    while i<m and j<n:
        if word[i] == abbr[j]:
            i, j = i+1, j+1
        elif abbr[j] == '0':
            return False
        elif abbr[j].isnumeric():
            k = j
            while k<n and abbr[k].isnumeric():
                k += 1
            i += int(abbr[j:k])
            j = k
        else:
            return False
    return i ==m and j == n
# print (P408_validWordAbbrevation('internationalization','i12iz4n'))

def P414_thirdMax(nums):
    maximum = set()
    for num in nums:
        maximum.add(num)
        if len(maximum) > 3:
            maximum.remove(min(maximum))
    if len(maximum) == 3:
        return min(maximum)
    return max(maximum)
# print (P414_thirdMax([2,2,3,1]))

def P415_addStrings(num1,num2):
    num1, num2 = list(num1), list(num2)
    res, carry = [], 0
    while len(num1)>0 or len(num2)>0:
        d1 = ord(num1.pop()) - ord('0') if len(num1)>0 else 0
        d2 = ord(num2.pop()) - ord('0') if len(num2)>0 else 0
        temp = d1 + d2 + carry
        res.append(str(temp%10))
        carry = int(temp/10)
    if carry: res.append(str(carry))
    result = ''.join(res)
    return result[::-1]
# print(P415_addStrings('123','123'))

def P437_pathSum(root,target):
    def dfs(node, target):
        if node is None:
            return 
        test(node,target)
        dfs(node.left, target)
        dfs(node.right, target)
    
    def test(node,target):
        nonlocal numOfPaths
        if node is None:
            return 
        if node.val == target:
            numOfPaths += 1
        test(node.left, target-node.val)
        test(node.right, target-node.val)

    numOfPaths = 0
    dfs(root,target)
    return numOfPaths
# print (P437_pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))),8))


def P443_compress(chars):
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read+1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read-anchor+1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    print (chars[:write])
    return write
# print (P443_compress(["a","a","b","b","c","c","c"]))


def P448_findDisappeardNumbers(nums):
    for i in range(len(nums)):
        new_index = abs(nums[i]) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1
    result = []
    for i in range(1, len(nums)+1):
        if nums[i-1]> 0:
            result.append(i)
    return result
# print (P448_findDisappeardNumbers([4,3,2,7,8,2,3,1]))


def P461_hammingDistance(x,y):
    def f1(x,y):
        return bin(x^y).count('1')
    def f2(x,y):
        xor = x^y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance
    def f3(x,y):
        xor, distance = x^y, 0
        while xor:
            distance += 1
            xor = xor & (xor -1)
        return distance
    f2(x,y)
    f3(x,y)
    return f1(x,y) 
# print (P461_hammingDistance(3,4))

def P463_islandPerimeter(grid):
    def edges(x):
        if not x: return 0
        count = 0
        for row in x:
            temp = [0] + row + [0]
            for i in range(len(temp)-1):
                if temp[i] != temp[i+1]:
                    count += 1
        return count
    Tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i,v in enumerate(row):
            Tgrid[i].append(v)
    return edges(grid)+edges(Tgrid)
# print (P463_islandPerimeter([[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]))


def P496_nextGreaterElement(nums1,nums2):
    d, stack, ans = {}, [], []
    for x in nums2:
        while len(stack) and stack[-1] < x:
            d[stack.pop()] = x
        stack.append(x)
    for x in nums1:
        ans.append(d.get(x,-1))
    return ans
# print (P496_nextGreaterElement([4,1,2],[1,3,4,2]))

def P543_diameterOfBinaryTree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if node is None: return 0
        L = dfs(node.left)
        R = dfs(node.right)
        ans = max(ans,L+R)
        return max(L,R) + 1
    dfs(root)
    return ans
# print (P543_diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),TreeNode(3))))

def P572_isSubtree(s,t):
    def equal(x,y):
        if x is None and y is None:
            return True
        if x is None or y is None:
            return False
        return x.val == y.val and equal(x.left,y.left) and equal(x.right,y.right)
    def traverse(s,t):
        return s is not None and (equal(s,t) or traverse(s.left,t) or traverse(s.right,t))
    return traverse(s,t)
# print (P572_isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2))))


def P628_maximumProduct(nums):
    def m1(nums):
        sorted(nums)
        return max (nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
    def m2(nums):
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        for n in nums:
            if n<= min1:
                min2,min1 = min1, n
            elif n < min2:
                min2 = n
            
            if n>=max1:
                max3,max2,max1 = max2,max1,n
            elif n >= max2:
                max3, max2 = max2, n
            elif n >= max3:
                max3 = n
        return max(min1*min2*max1, max1*max2*max3)
    m1(nums)
    return m2(nums)
# print (P628_maximumProduct([1,2,3,4]))

def P637_averageOfLevels(root):
    info = []
    def dfs(node, depth=0):
        if node:
            if len(info) <= depth:
                info.append([0,0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
    dfs(root)
    return [s/float(c) for s,c in info]
# print (P637_averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

def P653_findTarget(root,k):
    if root is None: return False
    bfs, s = [root], set()
    for node in bfs:
        if k-node.val in s:
            return True
        s.add(node.val)
        if node.left: bfs.append(node.left)
        if node.right: bfs.append(node.right)
    return False
# print (P653_findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))),9))

def P674_findLengthOfLCIS(nums):
    ans = i = 0
    while i < len(nums):
        curr_len = 1
        while i+1 < len(nums) and nums[i] < nums[i+1]:
            curr_len, i = curr_len + 1, i+1
        ans = max(ans,curr_len)
        i += 1
    return ans
# print (P674_findLengthOfLCIS([1,3,5,4,7]))

def P680_validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left+1:right+1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1 , right -1
    return True
# print (P680_validPalindrome('abca'))

import heapq
def P703_KthLargest():
    def __init__(self,k,nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool)> k:
            heapq.heappop(self.pool)
    def add(self,val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool,val)
        return self.pool[0]
    

def P724_pivotIndex(nums):
    left, right = 0, sum(nums)
    for i,x in enumerate(nums):
        right -= x
        if left == right:
            return i
        left += x
    return -1
# print (P724_pivotIndex([1, 7, 3, 6, 5, 6]))

def P733_floodFill(image,sr,sc, newColor):
    def dfs(i,j):
        image[i][j] = newColor
        for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=x<m and 0<=y < n and image[x][y] == old:
                dfs(x,y)
    old, m, n = image[sr][sc], len(image), len(image[0])
    if old != newColor:
        dfs(sr,sc)
    return image
# print(P733_floodFill([[1,1,1],[1,1,0],[1,0,1]],sr = 1, sc = 1, newColor = 2))

def P766_isToeplitzMatrix(matrix):
    return all (r==0 or c==0 or matrix[r-1][c-1]==val 
                    for r, row in enumerate(matrix)
                    for c, val in enumerate(row))
# print(P766_isToeplitzMatrix([
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]))

def P771_numJewelsInStones(J,S):
    Jset = set(J)
    return sum(s in Jset for s in S)
# print (P771_numJewelsInStones(J = "aA", S = "aAAbbbb"))

def P784_letterCasePermutation(S):
    res =['']
    for ch in S:
        if ch.isalpha():
            res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i+ch for i in res]
    return res
# print (P784_letterCasePermutation('1223'))

def P788_rotatedDigits(N):
    ans = 0
    for x in range(1,N+1):
        S = str(x)
        ans += all(d not in '347' for d in S) and any( d in '2569' for d in S)
    return ans
# print (P788_rotatedDigits(10))

def P852_peakIndexInMountainArray(A):
    lo, hi = 0, len(A) - 1
    while lo < hi:
        mi = (lo+hi)//2
        if A[mi] < A[mi+1]:
            lo = mi + 1
        else:
            hi = mi
    return lo
# print (P852_peakIndexInMountainArray([0,2,1,0]))

def P872_leafSimilar(root1, root2):
    def findLeaf(root):
        if root is None: return []
        if root.left is None and root.right is None: return [root.val]
        return findLeaf(root.left)+findLeaf(root.right)
    return findLeaf(root1) == findLeaf(root2)

def P893_numSpecialEquivGroups(A):
    def count(A):
        ans = [0]* 52
        for i, letter in enumerate(A):
            ans[ord(letter)-ord('a')+26*(i%2)] += 1
        return tuple(ans)
    return len({count(word) for word in A})
# print (P893_numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))


def P896_isMonotonic(A):
    ins = des = True
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            ins = False
        if A[i] < A[i+1]:
            des = False
    return ins or des
# print (P896_isMonotonic([1,2,2,3]))

def P905_sortArrayByParity(A):
    i,j = 0, len(A) -1
    while i < j:
        if A[i]%2 > A[j]%2:
            A[i], A[j] = A[j], A[i]
        if A[i]%2 ==0: i+= 1
        if A[j]%2 ==1: j-= 1
    return A
# print (P905_sortArrayByParity([3,1,2,4]))

def P938_rangeSumBSTRecursive(root,L,R):
    def dfs(node):
        nonlocal ans
        if node:
            if L<= node.val <= R:
                ans += node.val
            if L < node.val: dfs(node.left)
            if R > node.val: dfs(node.right)
    ans = 0
    dfs(root)
    return ans

def P938_rangeSumBSTIterative(root,L,R):
    ans = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if L<= node.val <= R:
                ans += node.val
            if L< node.val: stack.append(node.left)
            if R> node.val: stack.append(node.right)
    return ans

def P953_isAlienSorted(words,order):
    ind = {c:i for i,c in enumerate(order)}
    for a,b in zip(words,words[1:]):
        if len(a) > len(b) and a[:len(b)] == b:
            return False
        for s1,s2 in zip(a,b):
            if ind[s1] < ind[s2]:
                break
            elif ind[s1] > ind[s2]:
                return False
    return True
# print(P953_isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))


def P977_sortedSquare(A):
    i,j = 0, len(A)-1
    result = []
    while i<=j:
        if A[i]**2 <= A[j]**2:
            result.append(A[j]**2)
            j -= 1
        else:
            result.append (A[i]**2)
            i += 1
    return result[::-1]
# print (P977_sortedSquare([-4,-1,0,3,10]))


def P989_addToArrayForm(A,K):
    A[-1] += K
    for i in range(len(A)-1,-1,-1):
        carry, A[i] = divmod(A[i],10)
        if i: A[i-1] += carry
    if carry: A= map(int,str(carry)) + A
    return A
# print (P989_addToArrayForm(A = [1,2,0,0], K = 34))

def P997_findJudge(N,trust):
    if len(trust) < N-1: return -1
    score = [0]* (N+1)
    for a,b in trust:
        score[a], score[b] = score[a] -1, score[b] + 1
    for i,score in enumerate(score[1:],1):
        if score == N -1:
            return i
    return -1
# print (P997_findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))

def P1021_removeOuterParantheses(S):
    result = []
    count = 0
    for ch in S:
        if ch == '(': count += 1
        elif ch == ')': count -= 1
        if ch =='(' and count == 1: continue
        if ch == ')' and count == 0: continue
        result.append(ch)
    return ''.join(result)
# print(P1021_removeOuterParantheses('(()())(())(()(()))'))


def P1213_arraysIntersection(arr1,arr2, arr3):
    i = j = k = 0
    result = []
    while i<len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i,j,k = i+1, j+1, k+1
            continue
        max_ = max(arr1[i],arr2[j],arr3[k])
        i = i+1 if arr1[i] < max_ else i
        j = j+1 if arr2[j] < max_ else j
        k = k+1 if arr3[k] < max_ else k
    return result
print (P1213_arraysIntersection(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))
