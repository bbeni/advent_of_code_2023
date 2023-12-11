import math
import numpy as np
from itertools import combinations

with open(0) as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

m = []
for l in lines:
    m.append([1 if v=="#" else 0 for v in l])

def add_rows(m):
    m_res = m.copy()
    n = 0
    for i, x in enumerate(m):
        if (np.array(x) == 0).all():
            m_res.insert(i+n, x)
            n += 1
    return m_res

def trans(m):
    l1 = len(m)
    l2 = len(m[0])

    m2 = list([[-1 for l in range(l1)] for _ in range(l2) ])

    for i in range(len(m[0])):
        for j in range(len(m)):
            m2[i][j] = m[j][i]
    return m2

#m = list(m)
#m = add_rows(m)
#m = add_rows(trans(m))
indices = np.argwhere(np.matrix(m) == 1)
m = np.matrix(m)

rows = [1000000 if (m[i] == 0).all() else 1 for i in range(m.shape[0]) ]
cols = [1000000 if (m[:,i] == 0).all() else 1 for i in range(m.shape[1]) ]


def metric(x, y, m):
    d = 0
    a, b = min(x[0], y[0]), max(x[0], y[0])
    for i in range(a, b):
        d+=rows[i]
    #d = sum(rows[a:b])
    a, b = min(x[1], y[1]), max(x[1], y[1])
    for i in range(a, b):
        d+=cols[i]
    #d += sum(cols[a:b])
    return d


s = 0
for x, y in combinations(indices, 2):
    s+= metric(x, y, m)

print(s)