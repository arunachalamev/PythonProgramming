

def invalidTransactions(transactions):
    NAME,TIME,AMOUNT,CITY = range(4)

    txn = []
    for row in transactions:
        name, time, amount, city = row.split(',')
        time = int(time)
        amount = float(amount)
        txn.append((name,time,amount,city))

    ans = []
    for i,tx1 in enumerate(txn):
        if tx1[AMOUNT] > 1000:
            ans.append(transactions[i])
            continue
        for j,tx2 in enumerate(txn):
            if (i !=j and tx1[NAME] == tx2[NAME] and abs(tx2[TIME]-tx1[TIME])<60 and tx1[CITY] != tx2[CITY]):
                ans.append(transactions[i])
                break
    
    return ans


print (invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
print (invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
print (invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"]))
