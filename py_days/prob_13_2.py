import numpy as np
from itertools import product

with open(0) as f:
    lines = [l.strip() for l in f.readlines()]
    lines.append('')

        
def find_reflections(m):
    all = []
    for i in range(m.shape[0]-1):
        start = max(0, 2*i +2 - m.shape[0])
        end = min(2*i+2, m.shape[0])
        a = m[start:i+1,:]
        b = m[i+1:end,:]

        if (b[::-1,:] == a).all():
            all.append(i)
    return all


def find_all(m):
    x_h = find_reflections(m)
    x_v = find_reflections(m.T)
    return (x_h, x_v)

def find_smudges(m):
    all = []
    for i, j in product(range(m.shape[0]), range(m.shape[1])):
        m[i][j] = 0 if m[i][j] == 1 else 1
        xd = find_reflections(m)
        if not xd in all and xd is not None:
            all.append(xd)
        m[i][j] = 0 if m[i][j] == 1 else 1
    return all

def find_smudges_all(m):
    b = sorted(find_smudges(m.T), key=lambda x: len(x))[-1]
    a = sorted(find_smudges(m), key=lambda x: len(x))[-1]
    return a, b

s = 0
buffer = []
for line in lines:
    if line == '':
        m = np.array(buffer)
        xs = find_all(m)
        xd = find_smudges_all(m)
        #print('start', xs)
        #print('diff ', xd)

        if xs[0] != xd[0]:
            # print('row', xd, xs)
            # row
            if xs[0] == []:
                t = xd[0][0]
            else:
                xd[0].remove(xs[0][0])
                t = xd[0][0]
            s += 100*(t+1)
        else:
            # column

            if xs[1] == []:
                t = xd[1][0]
            else:
                xd[1].remove(xs[1][0])
                t = xd[1][0]
            s += (t+1)




        buffer = []
        continue
    buffer.append([0 if c=='.' else 1 for c in line])


print(s)
