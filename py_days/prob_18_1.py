import sys
import numpy as np
sys.setrecursionlimit(62002)


earth = np.zeros((10000, 10000))
pos = np.array([int(earth.shape[0]/2), int(earth.shape[1]/2)])

earth[pos[0], pos[1]]=1

directions = {  "U": np.array([0,-1]),
                "D": np.array([0,1]),
                "L": np.array([-1,0]),
                "R": np.array([1,0]), }

for line in open(0):
    direction, n, color = line.strip().split(' ')
    n = int(n)
    d = directions[direction]
    for i in range(n):
        t = i*d+pos
        earth[t[1],t[0]] = 1
    pos = n*d+pos

# ?
inside = np.array([int(earth.shape[0]/2)+2, int(earth.shape[1]/2)+1])

def flood(p, depth):
    if earth[p[1]][p[0]] != 0 or depth == 0:
        return
    earth[p[1]][p[0]] = 1
    for d in directions.values():
        flood(p+d, depth-1)

flood(inside, 62000)
print(int(earth.flatten().sum()))







