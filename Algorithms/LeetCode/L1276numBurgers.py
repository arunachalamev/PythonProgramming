

# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

# Jumbo Burger: 4 tomato slices and 1 cheese slice.
# Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and 
# the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices 
# and cheeseSlices equal to 0 return [].


def numBurgers(tomatoSlices, cheeseSlices):
    if tomatoSlices%2 == 1:
        return []
    if 2*cheeseSlices <= tomatoSlices and tomatoSlices <= 4* cheeseSlices:
        return [tomatoSlices/2- cheeseSlices, 2*cheeseSlices - tomatoSlices/2]
    
    return []


print (numBurgers(16,7))

# Explanation
# tomate number t should not be odd,
# and it should valid that c * 2 <= t && t <= c * 4.

# From
# jumbo + small = cheese
# jumbo * 2 + small = tomate / 2

# We can get that
# jumb0 = tomate / 2 - cheese
# So that
# small = cheese * 2 - tomate / 2