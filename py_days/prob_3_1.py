import numpy as np
from scipy.ndimage import convolve
import re

'''Part One'''
with open(0) as f:
    lines = f.read()
    lines = lines.split('\n')
    print(lines)
    lb = len(lines[0])
    la = len(lines)
    print(la, lb)
    touching = np.ones((la,lb), dtype=np.int16)
    for i in range(la):
        for j in range(lb):
            touching[i][j] = 1 if lines[i][j] not in ".0123456789" else 0


    touching = 0 < convolve(touching, np.ones((3,3)))
    touching = touching.flatten()
    string = ''.join(lines)
    n = re.finditer('(\d+)', string )
    xs = []
    rs = []
    for i in n:
        print(i.group(0), i.start(), i.end())
        x = int(i.group(0))
        r = list(range(i.start(), i.end()))
        xs.append(x)
        rs.append(r)

    indices = np.where(touching)[0]
    print(indices)
    s = 0
    for i, j in zip(xs, rs):
        for q in j:
            if (q==indices).any():
                s+=i
                break
    print(s)

