def minimumSwap(s1,s2):
    countX, countY = 0, 0
    mismatch = 0
    for l,r in zip(s1,s2):
        if l != r:
            mismatch = mismatch + 1
            if l == 'x':
                countX = countX + 1
            elif l == 'y':
                countY = countY + 1

    if mismatch %2 == 1:
        return -1
    else:
        return int((countX)/2 + (countY)/2 + (countX%2))


print (minimumSwap("xx","yy"))
print (minimumSwap("xy","yx"))
print (minimumSwap("xx","xy"))
print (minimumSwap("xxyyxyxyxx","xyyxyxxxyx"))
print (minimumSwap("xxxyyy","yyyxxx"))

