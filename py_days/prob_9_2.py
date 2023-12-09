import numpy as np

games = []
for i,  l in enumerate(open(0)):
    l = l.strip()
    games.append(list( map(int,l.split(' '))))



all = np.int64(0)
for game in games:
    left_row = [game[0]]
    next = np.array(game)
    while(next.any()):
        next = next[1:] - next[:-1]
        first_n = next[0]
        left_row.append(first_n)
    
    acc = 0
    for a in left_row[::-1][1:]:
        acc = a - acc
    all += acc
    print(acc)
    print('next game')

print(all)