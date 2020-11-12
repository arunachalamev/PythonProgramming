from typing import List
from functools import lru_cache
import collections
import random
import heapq
import math,itertools
from math import log2, ceil


0014 Longest common prefix among the list of strings
Many methods available - Horizontal, vertical, Divide and conquer, Binary search
Get the minimum string based on the length of the string [min(strs, key= len)]
enumerate minstr:
    for s in main list:
        if s[i] != current ch from enumeration:
            return minstr[:i]

Follow up: LCP query called frequently. Trie



0053- contiguous subarray with maximum sum
M1: Divide and conquer O(N log N ) & O(log N)
M2: Greedy O(N) & O(1)
M3: DP - O(N) & O(1)

initialize maxsofar and maxendinghere to 0
for every x in the array:
    increment maxendinghere to x
    when maxendinghere falls below 0:
        assign maxendinghere = 0
    update maxsofar to max of maxsofar , maxendinghere
return maxsofar

initialzie maxsofar = first value of the array
for every pos from 1
    if previous postion > 0:
        current position value incremented to previous pos value
    update maxsofar to max of maxsofar , current position value
return maxsofar



0069 - sqrt (x)
1 - pocket calculator algorithm: e^1/2 log(x) - O(1) & O(1)
2 - Binary search - O(log N) & O(1)
3 - Recursion + Bit shifts - O(log N) & O(log N)
4 - Newtons method - O(log N) & O(1)

Binary search method:
initialize low and high to 2 and x integer divide 2
while low <= high:
    calculate mid
    if square of mid > x:
        update hi to mid - 1
    elif square of mid < x:
        update lo to mid + 1
    else:
        return mid
on exit return hi



0070 - climbing stairs
DP - recursive, bottom up 



0111- minimum depth of binary tree
we can solve using recursion; DFS iteration; BFS iteration

BFS:
base case: when root is none return 0
initialzie stack with (root,0) and ans = inf
while stack is not empty:
    pop stack
    if node is leaf: update ans
    stack append node.left, depth+1 and similary for node.right
    ** append only when it is not None
return ans


0118 - pascal triangle
initialize triangle to empty list
for i ranging to num_rows:
    initialzie row to None of length i+1
    assign 1 to start and end of row
    for j in range from 1 to 1 less than row length
        row [j] = triange[i-1][j-1] + triange[i-1][j]
    append row
return triangle result



0141 Linked list cycle
Method1: Hash table - O(n) & O(n)
Method2: Two pointer - O(n) & O(1)

we use two ptr - slow and fast pointing to header
while fast and fast.next is not none:
    update fast = fast.next.next
    update slow = slow.next
    if slow == fast:
        return True

If we come out of loop, we return False



0160- Intersection of two linked List
If either of headA or heabB is None, return None
Maintain two ptr - ptrA, ptrB to headA and headB
while PA is not PB, repeat:
    Assign PA to headB if pa is none else pa.next
    similarly assing pb to headA if pb is none else pb.next
return pa


0168 - Excel sheet column title
Assign temp with 'ZA...Y' 
if n < 26, we return temp[n%26]
while n>1:
    rem, updated n = n%26 , n interger divide 26
    append the result with temp[rem]

On exist form while, we join the reveresed result and return


0226 - determine if the permutation of the string could form a palindrome
we will add the char to temp set on the first visit 
and remove when you visit next time
return true if len of the temp is <= 1



0246 - strobogrammatic Number - looks same when rotated 180 deg eg: 69 
We can use set of tuple such that it contains ('6','9') all sto Number
Use two pointer mechanism - with i and j points to start and end
check nums[i],nums[j] not in d - return False
inc, dec i and j
On completion, return True


0371 - sum of two integer without + or -
We can write recursive or iterative method

Iterative method:
    while b is not equal to 0:
        we have c = a & b
        a = a^b
        b = c<< 1
    return a



0387 - first unique character in a string
create a collection counter on the string
enumerate the string:
    if count[current char] == 1:
        return pos
on exist from for loop return -1



0392 Check if s is subsequence of t
Method 1: we can use linear scan with time complexity = O(Max lenght of the string)
Method 2: Using binary search:
            Maintain the pos of character ch in T in a List by scanning and appending to the List
            initialize the start pos = 0
            for each ch in s:
                check the insert location by using bisect_left in idx[ch]
                if insert location equal to len of idx[ch] return False
                now update the pos = idx[ch][insert location] + 1
            when we run out of ch in s, return True

Follow up: one long T and many s 
We use trie to store all the matched S with node containing the value of the matched position
in T. For new string, we look for max prefix string and start from their




0404- sum of left leaves
Recursive , Iterative - O(N)

base condition: return 0
if current node contains left node as leaf:
    return node.left.val + call the recursive function on node.right
return recursive on node.left + recursive on node.right



0461 Hamming distance
construct xor between x and y
count the number of ones 
or use while , and with 1 and left shift operation strategy



0463 Island of the perimeter
Construct a transpose of the matrix
Call a subroutine edges on matrix and transpose matrix and add them together
Idea of edges subroutine:
    append 0 to start and end of the List
    increment the counter whenever two adjacent element are not same



0572 - subtree of Another tree
We will have two subroutine, namely - equal subroutine and traverse subroutine
In equal subroutine:
    if x and y node is none: return True
    if x or y is none: return False
    we then return x.val == y.val & left subtree equal & right subtree equal

if traverse subroutine:
    we check for below condition
        s is not empty 
        and (equal(s,t) or traverse(s left subtree, t) or traverse(s right subtree, t))

In main routine, call traverse(s,t)



0674 - longest increasing subsequnce
sliding window method
we will initialize ans and anchor to 0
loop through the array:
    if i is non zero and previous value >= current value, update anchor = i
    update ans as max(ans, i-anchor + 1)
return ans



0724 - Find pivot index Sum(left) == sum(right)
initialize left as 0 and right to sum of all numbers
for enumeration (nums):
    we subtract x from right
    if we satisfy left == right : return i
    then increment left with x

on exist from for loop return -1



0788 Number of good number ( where rotated digits are valid) till N
Scan from 1 to N+1
Convert the number as string
We use all and any construct to increament the counter
    Condition is: all ( d not in '347' for d in S)
                and any ( d in '2569' for d in S)

    ** 0,1,8 is not required



0832- Flipping an image - reverse row and invert the entries
Using enumeration, reverse the rows
Scan through the entries and invert them as x^1

Optimized idea:
using row[~i] to read from the end
scan every row till the middle using (len(row)+1)//2
invert using ^ 1 and swap row[i] and row[~i]



0852- peak index in a mountain array
Two pointer meachanism with binary search - O(log N)
initialize lo, hi as start and end of array
while lo < hi:
    calculate mid 
    if A[mid] < A[mid+1] (i,e comparing two adjacent values):
        lo = mid + 1
    else:
        hi = mid
on exist return lo [ since hi might be = or crossed over]



0905 - sort by parity
Two pointer mechanism where i is the start and j is end of the array
Repeat till i < j : 
    swap the i and j if the condition met for even and odd
    if num[i] is even, inc i
    if num[j] is odd, dec j



0977 - squares of sorted array
Two pointer mechanism 
repeat till i<=j:
    if square of i-th location <= square of j-th location
        append square of j-th location to result
        dec j
    else:
        append i-th square
        inc i
return result in reverse order



1021- remove outermost parantheses
scan the input string
    if open, inc counter
    elif close, dec counter
    if open and counter == 1 : continue
    if close and counter == 0: continue
    append the current character
return join of the result



1029 - Cost of lying 2N ppl to 2 city with minimum flying cost
Idea is to calculate the diff in cost of flying -i.e., A - B
Sort the diff cost
Then fly first N ppl to city A and last N ppl to city B





*******************************************

In test function with node and target as parameter:
    we will be updating nonlocal variable numofpaths
    base case: Node node return None
    if we met the condition node.val equals target:
        increment numofpaths
    then call test function of node.left, node.right with parameter updated as target - node.val

Time complexity is tricky

*********************************************


0593 - given 4 point, check valid squares
M1: Check all permutation
M2: Using sorting
    Sort based on x-axis and in case of tie sort based on y- axis
    point pattern will be p0,p1,p2,p3
    calculate p0p1,p1p3,p3p2,p2p0 as sides
    calculate p0p3, p1p2 as diagonal
    check the condition dist>0 and sides equal and diagonal equals
M3: Checking every case will result in 3 combination

All algo runtime - O(1) & O(1)
similar question - check for rectangle, check if rec are interseting.

p = sorted([p1, p2, p3, p4], key = lambda x:(x[0], x[1]))



0028 - Implement strStr()
M1: Substring - linear time slice O((N-L)L) & O(1)
M2: two pointer method - linear time slice O((N-L)L) & O(1)
M3: Rabin Karp - constant time - O(N) & O(1)
    We will have lambda fun to calculate int value(ord(ch)-ord('a')) of character
    for L char in Needle and Haystack
        calculate hash - i.e, h = [h*26 + lambda(char)]%2**31

    if needle hash == haystack hash: 
        return 0 as the position

    Calculate aL = pow(a,L,Modulus)
    for start from 1 to n-L+1:
        calculate new hash 
            (hash*a - to_remove_char * aL + include char) % modulus
        if new hash == ref hash
            return start
    return -1


*****
0065 Valid Number
    Due to many combination involved, we should consider using DFA

0161 One Edit distance
    Greedy
    Involves insert, delete, replace
    One pass algorithm - O(n) & O(n)
    Assing first string as smaller length string
    Scan every charcter of first string:
        when mismatch: it could be delete or replace wrto first string
    on exit return edge case len(s) + 1 == len(t)

    related problem - find min num of operation to convert w1 to w2


0199 Binary tree right side view
    dfs method
    appending to nonlocal variable
    visit right node first then visit left node
    when level is not in d, add the level and update max level


0670 Swap two position to make number maximum
    Brute force - O(N^3)
    Greedy - O(N)
    maxid to last position
    xi = yi = 0
    Scan the string representation of number from R to L
        if the current number is max so far, update maxid
        elif current number < number at max id
            update xi = i and yi = maxid
    on exit from for loop, swap xi and yi
    join the string, convert to int , return


0026 Remove Duplicates from sorted array in place
    Two pointer - O(n) & O(1)
    initialize l,r = 0, 1
    untill r < len of array:
        if value @ l and value @ r are equal:
            inc r
        otherwise:
            inc l
            assing value @ l = value @ r
            inc r
    return l+1 ( length of the sub array)


0311 Sparse matrix multiplication
    Usual i,j,k but we swap the loop of k and j
    for i, row in enumeartion (A)
        for k, elemA in enumeration of (row)
            if elemA:
                for j, elemB in  enumeration (B[k])
                    if elemB: c[i][j] += elemA * elemB


0340 Longest substring with atmost k distinct characters
    two ptr mechanism with hashmap maintaing char to pos mapping
    whenever we have length of hashmap > k, 
        emove min pos char (index) and update l = index + 1
    ans = max(ans,r-l)
    return ans


11-12-2020

283- Move zeros to the end in place
Two variable method
i - position of current processing location
Scan array using j variable:
    if value @ j is non-zero:
        swap i and j
        increment i
print nums


721 - Account merge
M1: using DFS [ Connected component finding ] 
sum a_i log a_i 
build graph and search is sum a_i
but we have sorting at the end, which inc the TC to sum a_i log a_i

We maintain 2 ds - graph which is a default dict of set
a dictionary - which maintains email to name mapping

preprocessing stage:
    for each account:
        extract name
        for each email:
            add a bidirectional edge b/w email and first email in the list
            ** bidirectional is important which is added graph set 
            [ achieved by two statement with x & y interchanged]
            add mapping from email to name

actual algo - we are gng to find the component and add the entries:

for each email in the graph:
    if that email is not visited yet:
        add the email to visited and insert to stack
        initialize the component to be null list
        perform the following operation untill stack is empty:
            pop the node from stack
            add the node to component
            for each neighbours of node ( calculated from graph[node])
                if nei not visited:
                    add nei to visited & stack
        on stack empty: 
            add to the result 
            i.e., name from email + sorted(components)

# M2: using Union-Find 
# TC : O(A log A) but if we use union by rank , we will have O(A)
# SC: O(A)   where A  = sum length of account[i]

# have naive implementation of DSU

# have dsu object
# email_to_name, email_to_id as empty dictionary
# i =0 
# for each account:
#     extract name
#     for each email:
#         add mapping from email to name
#         if email not in email_to_id dictionary
#             add entry to email_to_id dic
#             inc i
#         union(email_to_id(first acc),email_to_id(email))

# for email in email_to_name:
#     find the id from the dsu and append email to a collectionlist


684 - Return the redundant connection which converted a tree into graph
DFS - O(N^2) & O(N) for graph building
DSU - O(N) ~ amortized runtime & O(N)

DFS:
    intialzie graph as default dict of set
    for every edge in the list:
        initialize seen as empty set [initialization for each edge]
        if u in graph and v in graph and dfs(u,v) [ check for connected]:
            return [u,v]
        add the edge to the graph object -i.e, 
        graph[u] = v
        graph[v] = u

    in dfs(s,t):
        if source not in seen [ to avoid revisiting the same node]:
            add src to seen set
            if source == target : return True
            return True if any dfs(nei,target) is true for nei in graph[source]

DSU:
    we use union by rank methodology
    create a dsu object
    for each edge in the list:
        if dsu.union(*edges) return false:
            return edge


143: Reorder the list
Find the middle
Reverse the second half
    think about reusing prev pointer


Merge two list 
here first is assigned to head, second is assigned to prev
- second list is shorter than the first List
    so we will loop till second.next is not null



236: Lowest common Ancestor of a Binary Tree
Maintain dictionary for parent pointers
Iterate untill we find both p and q [equivalent p not in parent or q not in parent]
    pop the stack
    while traversing the left and righ node, save the parent pointers

intialize ancestor to empty set
while p
    add the p to ancestor
    move to his parent

while q not in ancestor:
    assign q to parent of q
return q