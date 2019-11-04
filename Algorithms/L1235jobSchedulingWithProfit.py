# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime , endTime and profit arrays, you need to output the maximum profit 
# you can take such that there are no 2 jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.


import bisect

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1  # trace back where the current job can fit
        if dp[i][1] + p > dp[-1][1]:        # decide to include the job or not - dp[i]= max(dp[i-1],profit including job i)
            dp.append([e, dp[i][1] + p])    # add the job endtime and profit
    return dp[-1][1]



print (jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
#The subset chosen is the first, fourth and fifth job.  Profit obtained 150 = 20 + 70 + 60.

print (jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
#The subset chosen is the first and fourth job. Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

print (jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))

