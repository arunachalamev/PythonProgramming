# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times).

def maxProfit(a):
    profit = 0

    for i in range(1,len(a)):
        if a[i]-a[i-1]>0:
            profit += a[i] - a[i-1]

    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
