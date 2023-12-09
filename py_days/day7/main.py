import re
from functools import partial, reduce
from collections import defaultdict, deque
from itertools import accumulate, \
                      batched, groupby, starmap, \
                      permutations, combinations     
from operator import itemgetter, attrgetter # sorted(x, key=..(2))
#import numpy as np

with open("input.txt") as f:
#with open("test.txt") as f:
    lines = f.readlines()
    

ordering = "AKQJT98765432"[::-1]

def win(a, b):
    set(a), set(b)

def value_hand(hand):
    x, bid = hand
    q = len(set(x))
    l = [x.count(c) for c in x]
    max_count = sorted(set(l))[::-1]
    hc = sorted(x)[::-1]

    sorted_set = sorted(set(x))[::-1]

    if q == 1:
        # 5 kind
        #return (6, hc[0], -1, -1, -1, -1)
        return (6, x[0], x[1], x[2], x[3], x[4])
    elif q == 2 and max_count[0] == 4:
        # 4k
        card_type_hc = sorted_set[0] if x.count(sorted_set[0]) == 1 else sorted_set[1]
        card_type_4k = sorted_set[0] if x.count(sorted_set[0]) == 4 else sorted_set[1]
        #return (5, card_type_4k, card_type_hc, -1, -1, -1)
        return (5, x[0], x[1], x[2], x[3], x[4])
    elif q == 2 and max_count[0] == 3:
        # full house
        a = sorted_set[0] if x.count(sorted_set[0]) == 3 else sorted_set[1]
        b = sorted_set[0] if x.count(sorted_set[0]) == 2 else sorted_set[1]

#        return (4, a, b, -1, -1, -1)
        return (4, x[0], x[1], x[2], x[3], x[4])
    elif q == 3 and max_count[0] == 2:
        #two pair
        if x.count(sorted_set[0]) == 1:
            a, b, c = sorted_set[1], sorted_set[2], sorted_set[0]
        elif x.count(sorted_set[1]) == 1:
            a, b, c = sorted_set[0], sorted_set[2], sorted_set[0]
        elif x.count(sorted_set[2]) == 1:
            a, b, c = sorted_set[0], sorted_set[1], sorted_set[0]
        else:
            raise Exception('asdfasfasdf')
        #return (2, a, b, c, -1, -1)
        return (2, x[0], x[1], x[2], x[3], x[4])

    elif q == 3 and max_count[0] == 3:
        # 3 kind
        if x.count(sorted_set[0]) == 3:
            a, b, c = sorted_set[0], sorted_set[1], sorted_set[2]
        if x.count(sorted_set[1]) == 3:
            a, b, c = sorted_set[1], sorted_set[0], sorted_set[2]
        if x.count(sorted_set[2]) == 3:
            a, b, c = sorted_set[2], sorted_set[0], sorted_set[1]
        #return (3, a, b, c, -1, -1)
        return (3, x[0], x[1], x[2], x[3], x[4])

    elif q == 4:
        #one pair
        if x.count(sorted_set[0]) == 2:
            a,b,c,d = sorted_set[0], sorted_set[1], sorted_set[2], sorted_set[3]
        if x.count(sorted_set[1]) == 2:
            a,b,c,d = sorted_set[1], sorted_set[0], sorted_set[2], sorted_set[3]
        if x.count(sorted_set[2]) == 2:
            a,b,c,d = sorted_set[2], sorted_set[0], sorted_set[1], sorted_set[3]
        if x.count(sorted_set[3]) == 2:
            a,b,c,d = sorted_set[3], sorted_set[0], sorted_set[1], sorted_set[2]

        #return (1, a, b, c, d, -1)
        return (1, x[0], x[1], x[2], x[3], x[4])
    if q == 5:
        #hc
        #return (0, sorted_set[0], sorted_set[1], sorted_set[2], sorted_set[3], sorted_set[4])
        return (0, x[0], x[1], x[2], x[3], x[4])   



current_hand = []
current_bids = []
for line in lines:
    line = line.strip()
    cards, bid = line.split(' ')
    bid = int(bid)
    #cards = sorted([ordering.index(c) for c in cards])[::-1]
    cards = [ordering.index(c) for c in cards]
    current_hand.append((cards, bid))
    current_bids.append(bid)

print(current_bids, current_hand)

values = [value_hand(hand) for hand in current_hand]
s_hand = sorted(values)[::-1]
print(s_hand)
s_bid = [x for _, x in sorted( zip(values, current_bids), key=lambda pair: pair[0])[::-1]]
print(s_bid)

s = 0
for x, b in enumerate(s_bid[::-1]):
    print(x+1, b)
    s += (x+1)*b

for x in zip(s_hand, s_bid):
    print(x)


print(s)

# 245457852 < x < 255542648
