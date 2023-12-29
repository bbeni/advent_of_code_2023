'''
frame 65 touches all edges
the map is 131 x 131 pixels
hmm.. there is a diamond shape cut out

(26501365 - 65)/131 = 202300 = n
this squared is the number of maps filled?

we cut out the diamond edges of the map in all corners
and count the number of bushes (#) in the remaining part
for the edges

               d
       d      ddd
d     ddd    ddddd
       d      ddd
               d
steps:
65  65+131  65+2*131 ...  ->   65 + n*131

inner maps:
1       5      13    ...  ->   2n*n + 2n + 1

boundary terms corners:
0c     16c     48c      
0      4       12    ...  ->   2n*n + 2n

n*n + n +1
n*n + n

new start:

we got even and odd

               o
       o      oeo
o     oeo    oeoeo
       o      oeo
               o

we always have odd boundaries 
boundary:
    4(n-1) cut corner terms
    4 pointy corner terms
    4n corner
inside:
    n**2 full even terms
    (n-1)**2 full odd terms

    
disclaimer: only works for input.txt but 
not examples input!!!!!!!!!!!!!!
'''
import numpy as np
from PIL import Image

n = 202300

lines=[l.strip() for l in open(0)]
side_length = len(lines[0])
mid = int(side_length/2)
grid = [list(l) for l in lines]
start = int("".join(lines).index("S")/len(lines)),"".join(lines).index("S")%len(lines[0])

def advance(N, start_positions, grid):
    '''
        Advance grid by N steps with given position list.
    '''
    grid = grid.copy()
    width, height = len(grid[0]), len(grid)
    last_positions = set(start_positions)
    
    for iterations in range(N):
        positions = set([])
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[x][y] == '#':
                    continue
                for i, j in ((1,0),(-1,0),(0,1),(0,-1)):
                    neighbor_to_check = x+i, y+j
                    if x<0 or y<0 or \
                        x>width-1 or y>height-1:
                        continue 
                    if neighbor_to_check in last_positions:
                        positions.add((x,y))
        last_positions = positions
    return set(positions)

def create_dbg_img(positions):
    '''
        Create a debug and use save('asdf.png')
    '''
    width, height = len(grid),len(grid[0])
    mid = int(width/2)
    matrix = np.zeros((width, height, 3), dtype=np.uint8)
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            r, g, b = 10, 205, 10
            if tile == '#':
                matrix[i, j] = [r, g, b]
            else:
                matrix[i, j] = [25, 255, 55]
    for pos in positions:
        matrix[pos[0], pos[1]] = [200,180,0]

    for p in [(0,mid), (mid,0), (width-1,mid), (mid,width-1)]:
        matrix[p[0], p[1]]=[0,0,0]
    return Image.fromarray(matrix, 'RGB')

outer_even_count = 0
outer_odd_count = 0
inner_even_count = 0
inner_odd_count = 0

for i in range(side_length):
    for j in range(side_length):

        # check for unreachable (specific to input data)
        if i > 0 and i < side_length-1 and j > 0 and j < side_length-1:
            if lines[i+1][j]=="#" and lines[i][j+1]=="#" \
            and lines[i-1][j]=="#" and lines[i][j-1]=="#":
                continue

        if i+j > 3*mid or i+j < mid or i-j > mid or i-j < -mid:
            # outer
            if (i+j)%2 == 0:
                # even
                if lines[i][j] in '.S':
                    outer_even_count += 1
            else:
                # odd
                if lines[i][j] in '.S':
                    outer_odd_count += 1
        else:
            # inner
            if (i+j)%2 == 0:
                # even
                if lines[i][j] in '.S':
                    inner_even_count += 1
            else:
                # odd
                if lines[i][j] in '.S':
                    inner_odd_count += 1

full_even = inner_even_count+ outer_even_count
full_odd = inner_odd_count+outer_odd_count

corners_cut_odd = []
for corner in [(0,0), (0,side_length-1), \
               (side_length-1,0), (side_length-1,side_length-1)]:
    positions = advance(side_length+mid-1, [corner], grid)
    corners_cut_odd.append(len(positions))

corners_even = []
for c in [(0,0), (0,side_length-1), \
          (side_length-1,0), (side_length-1,side_length-1)]:
    positions = advance(mid-1, [c], grid)
    corners_even.append(len(positions))

pointy_corners_odd = []
for c in [(0,mid), (mid,0), (side_length-1,mid), (mid,side_length-1)]:
    positions = advance(side_length-1, [c], grid)
    pointy_corners_odd.append(len(positions))


boundary = sum(pointy_corners_odd) + (n-1)*sum(corners_cut_odd) + \
           n*sum(corners_even)
inside = n**2 * full_even + (n-1)**2 * full_odd

total = boundary + inside
print(total)

# too low 599640313183430
# too low 612941060350651
#         612941134797232
# wron    612941136011038
# wrin    612936553126617
# IDK 615519404195832