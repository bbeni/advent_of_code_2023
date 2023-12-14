from copy import deepcopy

with open(0) as f:
    lines = f.readlines()
    grid = [list(l.strip()) for l in lines]
    fixed_grid = [list(l.strip().replace('O', '.')) for l in lines]

h, w = len(grid), len(grid[0])

def evaluate(grid):
    s = 0
    for i in range(w):
        for j in range(h):
            if grid[j][i] == 'O':
                s += h-j
    return s

def collapse_north(grid, fixed_grid):
    new_grid = deepcopy(fixed_grid)
    for i in range(w):
        v = 0
        for j in range(h):
            if grid[j][i] == 'O':
                new_grid[v][i] = 'O'
                v += 1
            if grid[j][i] == '#':
                v = j+1
    return new_grid

def rotate_right(grid):
    new_grid = deepcopy(grid)
    for i in range(w):
        for j in range(h):
            new_grid[i][j] = grid[::-1][j][i]
    return new_grid

def one_cycle(grid):
    new = collapse_north(grid, fixed_grid)
    new = rotate_right(new)
    
    new = collapse_north(new, fixed_grid1)
    new = rotate_right(new)

    new = collapse_north(new, fixed_grid2)
    new = rotate_right(new)

    new = collapse_north(new, fixed_grid3)
    new = rotate_right(new)
    return new
    
fixed_grid1 = rotate_right(fixed_grid)
fixed_grid2 = rotate_right(fixed_grid1)
fixed_grid3 = rotate_right(fixed_grid2)

grids = []
cycle_index = -1

for i in range(100000):
    grid = one_cycle(grid)
    if grid in grids:
        cycle_index = grids.index(grid)
        break
    grids.append(grid)


# print(len(grids), cycle_index, len(grids)-cycle_index)
# do the remaining cycles
rest = (10**9 - cycle_index -1) % (len(grids)-cycle_index)

for i in range(rest):
    grid = one_cycle(grid)

print(evaluate(grid))

