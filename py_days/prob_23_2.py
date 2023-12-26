import random
import sys
import time
import cProfile

sys.setrecursionlimit(30000)


grid = []
for line in open(0):
    grid.append(line.strip()
                .replace('>', '.')
                .replace('<', '.')
                .replace('^', '.')
                .replace('v', '.'))

width, height = len(grid[0]), len(grid)

hits = 0

def walk(current, path=()):
    global hits
    # next possible paths
    nexts = []
    for neighbouring in ((current[0]+1, current[1]),
                            (current[0]-1, current[1]),
                            (current[0], current[1]+1),
                            (current[0], current[1]-1)):
        
        if not (0 <= neighbouring[0] < height):
            continue

        if grid[neighbouring[0]][neighbouring[1]] == '#':
            continue

        if neighbouring in path:
            continue

        
        nexts.append(neighbouring)

    if len(nexts) == 1:
        return walk(nexts[0], path) + 1


    if len(nexts) == 0:
        if current[0] == height-1:
            hits+=1
            print('juhuu:', hits)
            return 1
        return -1203123123
    
    max_l = walk(nexts[0], (current,)+path)
    for next in nexts[1:]:
        n = walk(next, (current,)+path)
        if n> max_l:
            max_l = n
    return max_l +1

    #next_lengths = []
    #for next in nexts:
    #   next_lengths.append(walk(next, (current,)+path))
    #return max(next_lengths) + 1


def main():
    s = time.time()
    res = walk((0,1))
    print('took: ', time.time() - s)
    print(res-1)
    # too low 5102
    
main()