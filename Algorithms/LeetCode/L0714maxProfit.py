

def maxProfit(prices,fee):
    cash, hold = 0, -prices[0]
    for i in range(1,len(prices)):
        cash = max(cash,hold+prices[i]-fee)
        hold = max(hold,cash-prices[i])
        print (cash,hold)

    return cash

print (maxProfit([1, 3, 2, 8, 9, 10],2))