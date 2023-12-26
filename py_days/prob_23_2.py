from copy import deepcopy

grid = []
for line in open(0):
    grid.append(line.strip())

width, height = len(grid[0]), len(grid)

# only one hike with one starting coord
hikes = [[[0, 1]]]
finishers = []

# ugly brute force XD
for i in range(15000):
    # one step
    print('step ', i, len(hikes))

    new_paths = []
    to_delete = []
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
            nexts.append(neighbouring)

        if len(nexts) == 0:
            to_delete.append(hikes[hike_nr])
            if current[0] == height-1 and current[1] == width-2:
                #finishers.append(deepcopy(hikes[hike_nr]))
                finishers.append(len(hikes[hike_nr]))
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

    print('deleted paths: ', len(to_delete))
    for td in to_delete:
        hikes.remove(td)
    if len(hikes) == 0:
        break

print(max(finishers)-1)