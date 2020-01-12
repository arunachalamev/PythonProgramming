
def minFlips(a,b,c):
    my_dict = {'000':0,'001':1,'010':1,'011':0,'100':1,'101':0,'110':2,'111':0}

    bin_a, bin_b, bin_c = bin(a)[2:], bin(b)[2:], bin(c)[2:]

    n = max(len(bin_a),len(bin_b),len(bin_c))
    # print (n,len(bin_a))
    bin_a = bin_a.zfill(n)
    bin_b = bin_b.zfill(n)
    bin_c = bin_c.zfill(n)
    # print (bin_a,bin_b,bin_c)
    count =0
    for i,j,k in zip(bin_a,bin_b,bin_c):
        temp = i+j+k
        count = count + my_dict[temp]
    return count

print (minFlips(2,6,5)) #3
print (minFlips(4,2,7)) #1
print (minFlips(1,2,3)) #0

