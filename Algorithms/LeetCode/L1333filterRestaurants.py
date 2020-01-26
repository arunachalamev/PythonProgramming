

def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    filtereddata = []

    for x in restaurants:
        if veganFriendly:
            if x[3] <= maxPrice and x[4] <= maxDistance and x[2] == 1:
                filtereddata.append(x)
        else:
            if x[3] <= maxPrice and x[4] <= maxDistance:
                filtereddata.append(x)


    result = sorted(filtereddata, key=lambda x: (x[1],x[0]), reverse=True)
    output = []
    for x in result:
        output.append(x[0])

    return output
