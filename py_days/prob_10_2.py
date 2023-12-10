from PIL import Image
import numpy as np


with open(0) as f:
    lines = [l.strip() for l in f.readlines()]

for j, l in enumerate(lines):
    if 'S' in l:
        start = (l.index('S'),j)


def play_directional(this_move = (0,1)):
    n_s = np.zeros((len(lines), len(lines[0])))
    n=1
    current = start
    while True:

        current = current[0]+this_move[0], current[1]+this_move[1]


        if n_s[current[1], current[0]] == 0:
            n_s[current[1], current[0]] += n
        else:
            break
        
        pipe = lines[current[1]][current[0]]
        horizontal = this_move[0] != 0

        if pipe == 'L':
            if horizontal:
                next_move = (0,-1)
            else:
                next_move = (1,0)
        elif pipe == 'J':
            if horizontal:
                next_move = (0,-1)
            else:
                next_move = (-1,0)
            pass
        elif pipe == '7':
            if horizontal:
                next_move = (0,1)
            else:
                next_move = (-1,0)
        elif pipe == 'F':
            if horizontal:
                next_move = (0,1)
            else:
                next_move = (1,0)
        elif pipe == '|':
            next_move = this_move
        elif pipe == '-':
            next_move = this_move
        elif pipe == 'S':
            break
        else:
            print(n_s)
            assert(False)

        this_move = next_move

        n += 1

    return n_s

r1 = play_directional(this_move=(0,1))

x = np.zeros((r1.shape[0]*2+2, r1.shape[1]*2+2))
x[1:-1:2, 1:-1:2] = r1
mask = (x>0).astype(np.uint8)

ascending = list(range(1,1+int(np.max(x))))

for a, b in zip(ascending + [1],  [1]+ ascending):
    i, j = np.argwhere(x==a)[0], np.argwhere(x==b)[0]
    mid = ((i+j)/2).astype(np.uint16)
    mask[mid[0],mid[1]] = 1
    
# flood outside
def flood(m, start):
    if start[0] < 0 or start[0] >= m.shape[0]:
        return 
    if start[1] < 0 or start[1] >= m.shape[1]:
        return
    if (m[start[0], start[1]] == 1):
        return
    if (m[start[0], start[1]] == 0):
        m[start[0], start[1]] = 1
        flood(m, start + np.array([1,0]))
        flood(m, start + np.array([-1,0]))
        flood(m, start + np.array([0,-1]))
        flood(m, start + np.array([0,1]))

#im2 = Image.fromarray(r1.astype(np.int16)*200)
#im2.show()
#im2 = Image.fromarray(mask.astype(np.int16)*200)
#im2.show()

import sys; sys.setrecursionlimit(20000)
flood(mask, np.array([0,0]))

contracted = mask[1:-1:2, 1:-1:2].copy()

#im_arr = (contracted == 0).astype(np.uint8)*200
#im2 = Image.fromarray(mask.astype(np.int8)*200)
#im2.show()

n = (contracted == 0).astype(np.uint8).sum()

print(n)