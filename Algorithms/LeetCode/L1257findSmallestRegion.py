# You are given some lists of regions where the first region of each list includes all other regions in that list.
# Naturally, if a region X contains another region Y then X is bigger than Y.
# Given two regions region1, region2, find out the smallest region that contains both of them.
# If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.
# It's guaranteed the smallest region exists.

# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"

import collections

def findSmallestRegion(regions,region1,region2):

    parent = {}

    for row in regions:
        for i in range(1,len(row)):
            parent[row[i]] = row[0]

    # print (parent)

    chain = set([region1])

    while region1 in parent:
        region1 = parent[region1]
        chain.add(region1)
    
    while region2 not in chain:
        region2 = parent[region2]
    
    return region2


regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]

region1 = "Quebec"
region2 = "New York"


print (findSmallestRegion(regions,region1,region2))
