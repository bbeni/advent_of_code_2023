with open(0) as f:
    lines = [l.strip() for l in f.readlines()]
h, w = len(lines), len(lines[0])

s = 0
for i in range(w):
    v = h
    for j in range(h):
        if lines[j][i] == 'O':
            s += v
            v -= 1
        if lines[j][i] == '#':
            v = h-j-1

print(s)

