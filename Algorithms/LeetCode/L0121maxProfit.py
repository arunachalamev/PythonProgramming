# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

def maxProfit(a):
    profit = 0
    minPrice = a[0]

    for i in range(1,len(a)):
        if a[i]-minPrice > profit:
            profit = a[i] - minPrice
        if a[i] < minPrice:
            minPrice = a[i]
    
    return profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
