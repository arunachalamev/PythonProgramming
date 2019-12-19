import random
def shuffle(n):
    cards = list(range(n))
    for i in range(n):
        new_pos = random.randint(i,n-1)
        cards[i] , cards[new_pos] = cards[new_pos], cards[i]
    print (cards)
    return

shuffle(52)