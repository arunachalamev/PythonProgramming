
def numOfSubarrays(arr, k, threshold):
    if len(arr) == 0: return 0
    if len (arr) < k: return 0
    l = len(arr)
    count = 0
    runningSum = []
    runningSum.append(0)
    for i in range(l):
        runningSum.append(runningSum[-1] + arr[i])

    for i in range(k,l+1):
        temp = (runningSum[i] - runningSum[i-k])/k
        if temp >= threshold:
            count +=1

    return count
