import numpy as np
from copy import deepcopy

bricks = []
height_map = np.zeros((10,10))
space = np.zeros((10, 10, 300))

for line in open(0):
    x = list(map(int, line.strip().replace("~", ",").split(",")))
    a, b = x[:3], x[3:]
    bricks.append((a, b))

by_z = sorted(bricks ,key=lambda x: x[0][2])

bricks_relaxed = []

for id, brick in enumerate(by_z, 1):
    start = brick[0][:2]
    end = brick[1][:2]
    z = int(np.max(height_map[start[0]:end[0]+1, start[1]:end[1]+1])) 
    delta_z = brick[1][2] - brick[0][2]
    bricks_relaxed.append(((brick[0][0], brick[0][1], z),(brick[1][0], brick[1][1], z+delta_z)))
    space[start[0]:end[0]+1, start[1]:end[1]+1, z:z+delta_z+1] = id
 
    z += 1
    z += brick[1][2] - brick[0][2]
    height_map[start[0]:end[0]+1, start[1]:end[1]+1] = z
 

# search previous layers
supported_by = []
for id, brick in enumerate(bricks_relaxed, 1):
    start = brick[0][:2]
    end = brick[1][:2]
    zb = brick[0][2]-1
    x = space[start[0]:end[0]+1, start[1]:end[1]+1, zb]
    x= x.astype(np.int32).flatten().tolist()
    res = set(x)
    if 0 in res:
        res.remove(0)

    # add floor id
    if len(res) == 0:
        res.add(100000)

    supported_by.append(res)


def collapse(support, id, max_iter=2):
    if max_iter == 0:
        return support
    for x in support:
        if id in x:
            x.remove(id)
    for id_n, x in enumerate(support, 1):
        if len(x) == 0:
            support = collapse(support, id_n, max_iter-1)
    return support

s = 0
for id in range(1, len(supported_by)+1):
    print('doing', id)
    support = deepcopy(supported_by)
    res = len([x for x in collapse(support, id) if x==set()])
    s += res

print(s)

# 6362 too low
# 32 wrong