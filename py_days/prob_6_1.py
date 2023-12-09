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
    text = f.read()


time = map(int, re.findall('\\d+', lines[0]))
dist = map(int, re.findall('\\d+', lines[1]))

time = [int(''.join(map(str, time)))]
dist = [int(''.join(map(str, dist)))]
#print(time, dist)


tt = [(list(range(1,t)) ,d)  for t, d in zip(time, dist)]

result = 1
for tl, d in tt:
    #print(tl, d)
    long = []
    for i, t in enumerate(tl):
        if (i % 100000 == 0):
            print(i)
        lasts = tl[-1] + 1
        res = (lasts - t)*(i+1)
        if res > d:
            long.append(res)
            #print('z', res, lasts)
    result *= len(long)

print(result)