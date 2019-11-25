# Given an array of strings products and a string searchWord. We want to design a system that suggests 
# at most three product names from products after each character of searchWord is typed. 
# Suggested products should have common prefix with the searchWord. If there are more than three products 
# with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed. 

def suggestedProducts(products,searchWord):

    products.sort()
    temp = ""
    output = list()

    for char in searchWord:
        temp = temp + char
        result = [k for k in products if k.startswith(temp)]
        if len(result) > 3:
            output.append(result[:3])
        else:
            output.append(result)


    return output


print (suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))
print (suggestedProducts(["havana"],"havana"))
print (suggestedProducts(["havana"],"titanic"))

