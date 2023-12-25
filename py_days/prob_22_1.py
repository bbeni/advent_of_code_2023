from ast import Not
import numpy as np

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
 

# search next layers
supporting = []
for id, brick in enumerate(bricks_relaxed, 1):
    start = brick[0][:2]
    end = brick[1][:2]
    zb = brick[1][2]+1
    x = space[start[0]:end[0]+1, start[1]:end[1]+1, zb]
    x= x.astype(np.int32).flatten().tolist()
    res = set(x)
    if 0 in res:
        res.remove(0)
    supporting.append(res)

s = 0
for id, support in enumerate(supporting, 1):
    if len(supporting) == 0:
        s+=1
        continue
    
    # check every one in top layer and see if they have other supports
    others = supporting[:id-1] + supporting[id:]
    others = [item for row in others for item in row]
    
    good = True
    for id_s in support:
        if id_s not in others:
            good = False
    
    if good:
        s+=1



print(s)