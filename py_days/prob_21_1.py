lines=[l.strip() for l in open(0)]
grid = [list(l) for l in lines]

s = int("".join(lines).index("S")/len(lines)),"".join(lines).index("S")%len(lines[0])
positions = [s]

def update(x,y, char):
    if pos[0]<0 or pos[1]<0 or \
        pos[0]>len(grid)-2 or pos[1]>len(grid[0])-2:
        return
    if grid[x][y] == '#':
        return
    
    grid[x][y] = char
    return True

for i in range(64):
    new_pos = []
    for pos in positions:
        for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
            if update(pos[0]+x, pos[1]+y, 'O'):
                if (pos[0]+x, pos[1]+y) not in new_pos:
                    new_pos.append((pos[0]+x, pos[1]+y))
        update(pos[0], pos[1], '.')
    #print(positions)
    positions = new_pos

print(''.join([''.join(g) for g in grid]).count('O'))

# too high 8580