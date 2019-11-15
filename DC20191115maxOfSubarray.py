
import collections

def maxOfSubArray(input, k):
    result = list()
    dq = collections.deque()

    if len(input) <=3:
        return max(input)

    if not input:
        return None

    for i in range(k):
        while dq and input[dq[-1]]<input[i]:
            dq.pop()
        dq.append(i)

    result.append(input[dq[0]])

    for i in range(k,len(input)):
        while dq and dq[0] <= i-k:
            dq.popleft()

        while dq and input[dq[-1]]<input[i]:
            dq.pop()
        dq.append(i)

        result.append(input[dq[0]])

    return result

# print (maxOfSubArray([10,5,2,7,8,7],3))

assert (maxOfSubArray([10,5,2,7,8,7],3) == [10,7,8,8])

print ('Done')