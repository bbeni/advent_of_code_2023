import re
from functools import partial, reduce
from collections import defaultdict, deque
from itertools import accumulate, \
                      batched, groupby, starmap, \
                      permutations, combinations     
from operator import itemgetter, attrgetter # sorted(x, key=..(2))
#import numpy as np


with open(0) as f:
#with open("test.txt") as f:
    lines = f.readlines()
    

ordering = "AKQT98765432J"[::-1]


def value_hand(hand):
    x = hand

    card_counts = defaultdict(int)
    for i in x:
        card_counts[i] += 1 

    print(card_counts)

    n_different = len(card_counts)
    n_jokers = card_counts[0]
    sorted_by_ammount = sorted(card_counts.items(), \
                                key=lambda x:x[1])[::-1]

    print(sorted_by_ammount)
    max_ammount = sorted_by_ammount[0][1]

    ret = -1

    if n_jokers == 0:
        if n_different == 1: 
            ret = 6
        if n_different == 2:
            if max_ammount == 4:
                ret = 5  
            if max_ammount == 3:
                ret = 4
        if n_different == 3:
            if max_ammount == 3:
                ret = 3  
            if max_ammount == 2:
                ret = 2
        if n_different == 4:
            ret = 1
        if n_different == 5:
            ret = 0

    if n_jokers == 1:
        if n_different == 2:
            ret = 6
        if n_different == 3:
            if max_ammount == 3:
                ret = 5  
            if max_ammount == 2:
                ret = 4
        if n_different == 4:
            ret = 3
        if n_different == 5:
            ret = 1

    if n_jokers == 2:
        if n_different == 2:
            ret = 6
        if n_different == 3:
            ret = 5
        if n_different == 4:
            ret = 3

    if n_jokers == 3:
        if n_different == 2:
            ret = 6
        if n_different == 3:
            ret = 5

    if n_jokers == 4:
        ret = 6
    
    if n_jokers == 5:
        ret = 6
    
    print(ret, n_different, n_jokers)
    print(hand)
    assert(ret != -1)

    return (ret, x[0], x[1], x[2], x[3], x[4])





current_hand = []
current_bids = []
for line in lines:
    line = line.strip()
    cards, bid = line.split(' ')
    bid = int(bid)
    cards = [ordering.index(c) for c in cards]
    current_hand.append(cards)
    current_bids.append(bid)

#for hand in current_hand:
    #print(hand, value_hand(hand))


values = [value_hand(hand) for hand in current_hand]
s_hand = sorted(values)[::-1]
s_bid = [x for _, x in sorted( zip(values, current_bids), key=lambda pair: pair[0])[::-1]]

s = 0
for x, b in enumerate(s_bid[::-1]):
    s += (x+1)*b


print(s)

# 246514349  246554449  246648309< x  
# wrong: 247750709,248380161

