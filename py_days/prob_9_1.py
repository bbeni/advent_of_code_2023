import numpy as np

games = []
for i,  l in enumerate(open(0)):
    l = l.strip()
    games.append(list( map(int,l.split(' '))))



all = np.int64(0)
for game in games:
    acc = game[-1]
    next = np.array(game)
    while(next.any()):
        next = next[1:] - next[:-1]
        last_n = next[-1]
        acc+= last_n
        print(next)
    all += acc
    print(acc)
    print('next game')

print(all)