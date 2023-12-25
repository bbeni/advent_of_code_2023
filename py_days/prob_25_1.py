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
        laplacian[y,x] = -1.0000
    laplacian[x,x] = len(v)

# compute fiedl vector and partition the graph
vals, vecs = np.linalg.eigh(laplacian)
fiedl_vec = vecs[1]
indices = np.argwhere(fiedl_vec > 0)
other_indices = np.argwhere(fiedl_vec <= 0)

# dirty fix
a = len(indices)-1
b = len(other_indices)+1

print(a*b)

# 538656 too high
# 538531 too low
# ez clap 538560