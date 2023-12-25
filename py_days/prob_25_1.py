from collections import defaultdict
from itertools import combinations
import numpy as np

parts_dict = defaultdict(list)
connections = []

for line in open(0):
    parts = line.strip().replace(':', '').split(' ')
    a = parts[0]
    b = parts[1:]

    parts_dict[a].extend(b)
    for ib in b:
        parts_dict[ib].append(a)


d = {}
for k, v in parts_dict.items():
    d[k] = [i for i in set(v)]


# laplacian matrix build
laplacian = np.zeros((len(d), len(d)))
ordered = list(d.keys())
for k, v in d.items():
    x = ordered.index(k)
    for vi in v:
        y = ordered.index(vi)
        laplacian[x,y] = -1
        laplacian[y,x] = -1
    laplacian[x,x] = len(v)

def disconnect(x, y, laplacian):
    assert(x != y)
    if laplacian[x, y] == 0:
        return False
    laplacian[x, y] = 0
    laplacian[y, x] = 0
    laplacian[x, x] -= 1
    laplacian[y, y] -= 1
    return True

def connect(x, y, laplacian):
    assert(x != y)
    if laplacian[x, y] != 0:
        return
    laplacian[x, y] = -1
    laplacian[y, x] = -1
    laplacian[x, x] += 1
    laplacian[y, y] += 1

print(laplacian.trace())
x = np.argwhere(laplacian == -1)
print(len(x))

indices = list(range(len(ordered)))

cuts = list(combinations(indices, 2))
print(len(cuts))

m = 2
i = 0
for a, b, c in combinations(x, 3):
    if i%10 == 0:
        print(i/1000)
    q = disconnect(a[0], a[1], laplacian)
    v = disconnect(b[0], b[1], laplacian)
    w = disconnect(c[0], c[1], laplacian)

    if q and v and w:
        x = np.linalg.eigvals(laplacian)
        friedler_value = sorted(x)[1]
        if friedler_value<m:
            m = friedler_value
        if friedler_value <= 0.00001:
            print('found', friedler_value)
            break

    if q: connect(a[0], a[1], laplacian)
    if v: connect(b[0], b[1], laplacian)
    if w: connect(c[0], c[1], laplacian)
    i += 1


print(a, b, c)
print(ordered[a[0]], ordered[a[1]])
print(ordered[b[0]], ordered[b[1]])
print(ordered[c[0]], ordered[c[1]])
print(friedler_value)