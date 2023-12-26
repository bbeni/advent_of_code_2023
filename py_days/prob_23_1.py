from copy import deepcopy

grid = []

for line in open(0):
    grid.append(line.strip())

width, height = len(grid[0]), len(grid)


# only one hike with one starting coord
hikes = [[[0, 1]]]

for i in range(2500):
    # one step
    print('step ', i)

    new_paths = []
    for hike_nr in range(len(hikes)):
        current = hikes[hike_nr][-1]
        nexts = []
        for neighbouring in [[current[0]+1, current[1]],
                             [current[0]-1, current[1]],
                             [current[0], current[1]+1],
                             [current[0], current[1]-1]]:
            if not (0 <= neighbouring[0] < height and 0 <= neighbouring[1] < width):
                continue
            if neighbouring in hikes[hike_nr]:
                continue
            tile = grid[neighbouring[0]][neighbouring[1]]
            if tile == '#':
                continue
            
            if neighbouring[0] - current[0] == 1 and tile =='^':
                continue
            if neighbouring[0] - current[0] == -1 and tile =='v':
                continue
            if neighbouring[1] - current[1] == -1 and tile =='>':
                continue
            if neighbouring[1] - current[1] == 1 and tile =='<':
                continue
            nexts.append(neighbouring)

        if len(nexts) == 0:
            continue
        elif len(nexts) == 1:
            hikes[hike_nr].append(nexts[0])
        elif len(nexts) == 2:
            new_paths.append(deepcopy(hikes[hike_nr]))
            new_paths[-1].append(nexts[1])
            hikes[hike_nr].append(nexts[0])

        elif len(nexts) == 3:
            new_paths.append(deepcopy(hikes[hike_nr]))
            new_paths[-1].append(nexts[1])
            new_paths.append(deepcopy(hikes[hike_nr]))
            new_paths[-1].append(nexts[2])
            hikes[hike_nr].append(nexts[0])
        else:
            assert(False)
    hikes.extend(new_paths)

print(max(map(len, hikes))-1)





