'''
notes:
======
only works for small input sizes
need a better idea

'''
import numpy as np
import sys
sys.setrecursionlimit(10000)

lines = [line.strip() for line in open(0).readlines()]

grid = [list(map(int, line)) for line in lines]
grid = np.array(grid)
WIDTH = grid.shape[0]

def create_shifted_plus(x_shift, y_shift, grid, pad=3):
    grid_padded = np.zeros((grid.shape[0]+pad*2, grid.shape[1]+pad*2))
    grid_padded[:,:] = np.Infinity
    grid_padded[pad:-pad-99,pad:-pad-99] = grid[:-99,:-99]
    grid2 = grid_padded.copy()

    assert( x_shift == 0 or y_shift == 0 )
    if y_shift:
        step = np.sign(y_shift)
        for y in range(step, y_shift+step, step):
            end = None if -pad-y == 0 else -pad-y
            grid2[:,pad:-pad] += grid_padded[:,pad-y:end]
    else:
        step = np.sign(x_shift)
        for x in range(step, x_shift+step, step):
            end = None if -pad-x == 0 else -pad-x
            grid2[pad:-pad,:] += grid_padded[pad-x:end,:]

    return grid2[pad:-pad, pad:-pad] - grid

def best_path(start, end, length, dir_idx, vertical=True):
    x, y = start
    if (x+y+1)*9 < length:
        return
    if start[0] < 0 or start[0] >= WIDTH or start[1] < 0 or start[1] >= WIDTH:
        return
    if length > min_so_far[x, y, dir_idx]:
        return 
    min_so_far[x, y, dir_idx] = length
    if start == end:
        print('found', length, x, y)
        return

    if vertical:
        for i in [3,-3,2,-2,1,-1]:
            l = length + LR[i][x,y]
            best_path((start[0], start[1]+i), end, l, i, False)
    else:
        for i in [3,-3,2,-2,1,-1]:
            l = length + UD[i][x,y]
            best_path((start[0]+i, start[1]), end, l, i, True)

# create L R U D matrices shifted by 1,2,3 in both directions
UD = [create_shifted_plus(a,0,grid) for a in [-1,-2,-3,3,2,1]]
LR = [create_shifted_plus(0,a,grid) for a in [-1,-2,-3,3,2,1]]

# dummy index to be able to acess UD[1] as first
UD.insert(0, None)
LR.insert(0, None)


# x, y,  dummy + direction index
min_so_far = np.zeros((WIDTH, WIDTH, 7))
min_so_far[:,:] = 100000000

start = (0, 0)
end = (WIDTH-100, WIDTH-100)
x = best_path(start, end, 0, 0, vertical=True)
print(np.min(min_so_far[end[0], end[1],:]))

# 1245 too high