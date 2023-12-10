import numpy as np

with open(0) as f:
    lines = [l.strip() for l in f.readlines()]

for j, l in enumerate(lines):
    if 'S' in l:
        start = (l.index('S'),j)


def play_directional(this_move = (0,1)):
    n_s = np.zeros((len(lines[0]), len(lines)))
    n=1
    current = start
    while True:

        current = current[0]+this_move[0], current[1]+this_move[1]

        if n_s[current[1], current[0]] == 0:
            n_s[current[1], current[0]] += n
        else:
            break
        
        pipe = lines[current[1]][current[0]]
        horizontal = this_move[0] != 0

        if pipe == 'L':
            if horizontal:
                next_move = (0,-1)
            else:
                next_move = (1,0)
        elif pipe == 'J':
            if horizontal:
                next_move = (0,-1)
            else:
                next_move = (-1,0)
            pass
        elif pipe == '7':
            if horizontal:
                next_move = (0,1)
            else:
                next_move = (-1,0)
        elif pipe == 'F':
            if horizontal:
                next_move = (0,1)
            else:
                next_move = (1,0)
        elif pipe == '|':
            next_move = this_move
        elif pipe == '-':
            next_move = this_move
        elif pipe == 'S':
            break
        else:
            print(n_s)
            assert(False)

        this_move = next_move

        n += 1

    return n_s

        

r1 = play_directional(this_move=(0,1))
x = int(np.max(r1)/2)

print(x)