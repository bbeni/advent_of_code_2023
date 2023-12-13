import numpy as np

with open(0) as f:
    lines = [l.strip() for l in f.readlines()]
    lines.append('')

def find_reflection(m):
    for i in range(m.shape[0]-1):
        start = max(0, 2*i +2 - m.shape[0])
        end = min(2*i+2, m.shape[0])
        a = m[start:i+1,:]
        b = m[i+1:end,:]

        if (b[::-1,:] == a).all():
            return i


s = 0
buffer = []
for line in lines:
    if line == '':
        m = np.array(buffer)
        x = find_reflection(m)
        if x is not None:
            s += 100*(1+x)
        else:
            x = find_reflection(m.T)
            s += (1+x)

        buffer = []
        continue
    buffer.append([0 if c=='.' else 1 for c in line])


print(s)
