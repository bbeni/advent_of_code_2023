import re
with open(0) as f:
    lines = f.readlines()

## part two
seeds = lines[0].split(':')[1].strip().split(' ')
seeds = [int(s) for s in seeds]
seeds_range = [ (a, a+b-1) for a, b in zip(seeds[::2], seeds[1::2])]

maps = []

for line in lines[1:]:
    if line == '\n':
        maps.append([])
    numbers = re.findall(r'\d+', line)
    if len(numbers) > 0:
        maps[len(maps)-1].append(list(map(int, numbers)))

def intersection(r1, r2):
    a, b = r1
    c, d = r2
    q, v = max(a, c), min(b, d)
    if q > v:
        return None
    else:
        return (q, v)
    
def exclusion(r1, r2):
    '''exclude r2 from r1 if possible'''
    x = intersection(r1, r2)
    if x is None:
        return r1,
    #split it
    if x[0] > r1[0] and x[1] < r1[1]:
        return (r1[0], x[0]-1), (x[1]+1, r1[1])
    if x[0] == r1[0] and x[1] == r1[1]:
        return ()
    if x[0] == r1[0]:
        return (x[1]+1, r1[1]),
    if x[1] == r1[1]:
        return (r1[0], x[0]-1),
    return x,
    
    
def remove(r_list, r):
    gathering = []
    for remaining in r_list:
        x = exclusion(remaining, r)
        gathering.extend(x)
    return gathering


#print(seeds_range)
current = seeds_range
for map in maps:
    next = []
    rest = []
    for seed in current:
        remaining = [seed]
        for a, b, l in map:
            start = (b, b+l-1)
            x = intersection(seed, start)
            #print('i', seed, start, x)
            if x:
                diff = a - b
                n = (x[0] + diff, x[1] + diff)
                next.append(n)
                remaining = remove(remaining, x)
        rest.extend(remaining)
    next.extend(rest)
    current = next

print(min(current)[0])


# tests
if False:
    x = intersection((1,10), (2,3))
    print(x)
    x = intersection((1,10), (1,3))
    print(x)
    x = intersection((1,10), (2,3))
    print(x)

    x = exclusion((1,10), (2,3))
    print(x)
    x = exclusion((1,10), (1,3))
    print(x)
    x = exclusion((1,10), (1,10))
    print(x)
    x = exclusion((1,10), (5,10))
    print(x)
    x = exclusion((1,10), (10,12))
    print(x)
    x = exclusion((1,10), (11,15))
    print(x)

    
