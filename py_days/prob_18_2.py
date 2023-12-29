''' slow but works '''

from itertools import pairwise, product
import matplotlib.pyplot as plt

instructions = []
for line in open(0):
    x = line.strip().split('#')[-1]
    a, b = x[:-2], x[-2:-1]
    direction = {'0':(1,0), '1':(0,1), '2':(-1,0), '3':(0,-1)}[b]
    dist = int(a, 16)
    instructions.append((dist, direction))

x_values = set()
y_values = set()
corners = [(0,0)]
for leng, dir in instructions:
    prev = corners[-1]
    vertex = prev[0] + dir[0]*(leng), prev[1] + dir[1]*(leng)
    corners.append(vertex)
    x_values.add(vertex[0])
    y_values.add(vertex[1])

length_of_boundary = 0
edges = []
for v1, v2 in pairwise(corners):
    edges.append((v1, v2))
    length_of_boundary += abs(v1[0]-v2[0]+v1[1]-v2[1])

def ccw(a, b, c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])

def intersects(e1, e2):
    # check if edges e1 and e2 intersect
    # stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
    (a, b), (c, d) = e1, e2
    return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)

rectangle_midpoints = []
areas = []
for (x1, x2), (y1, y2) in \
    product(pairwise(sorted(x_values)), pairwise(sorted(y_values))):
    a, b = x2-x1, y2-y1
    areas.append(a*b)
    rectangle_midpoints.append((x1 + a/2, y1 + b/2))

vertical_edges = list(filter(lambda  x: x[0][1] == x[1][1], edges))



i_counts = []

top = max(y_values)+1
s = 0
for rect, area in zip(rectangle_midpoints, areas):

    # shoot to the top
    intersection_count = 0
    for edge in vertical_edges:
        if intersects(edge, (rect, (rect[0], top))):
            intersection_count += 1
    if intersection_count % 2 == 1:
        s += area
    i_counts.append(intersection_count)

print(int(s+length_of_boundary/2+1))

# too high 264268309852389
# too low  250022064876277

debug = True
if debug:
    for rect, i in zip(rectangle_midpoints, i_counts):
        plt.plot(rect[0], rect[1], 'x')
        plt.annotate(str(i), (rect[0], rect[1]))
        #plt.plot([rect[0], rect[0]], [rect[1], top])

    n = [a for a, b in corners]
    m = [b for a, b in corners]
    plt.plot(n,m)
    plt.show()