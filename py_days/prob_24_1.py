from itertools import combinations

coords = []
velocities = []
for line in open(0):
    a, b = line.strip().split('@')


    coords.append(tuple(map(int,a.split(', ')))[:2])
    velocities.append(tuple(map(int,b.split(', ')))[:2])


left, right = 7, 27

# real input values
if len(coords) > 7:
    left, right = 200000000000000, 400000000000000

def intersects(r1, v1, r2, v2):
    x1, y1 = r1
    x3, y3 = r2

    a1, b1 = v1
    a2, b2 = v2

    x2 = a1 + x1
    y2 = b1 + y1

    x4 = a2 + x3
    y4 = b2 + y3

    d = ((x1 - x2)*(y3-y4) -(y1-y2)*(x3-x4))
    if d == 0:
        return None

    t = ((x1 - x3)*(y3-y4) - (y1-y3)*(x3-x4))/d
    u = ((x1 - x3)*(y1-y2) - (y1-y3)*(x1-x2))/d

    if u>=0 and t>= 0:
        return (x1 + t*a1, y1 + t*b1)
    return None


s = 0
for a, b in combinations(zip(coords, velocities), 2):
    intersection = intersects(a[0], a[1], b[0], b[1])
    if intersection is None:
        continue
    if intersection[0] >= right or intersection[0] <= left:
        continue
    if intersection[1] >= right or intersection[1] <= left:
        continue

    s+=1

print(s)