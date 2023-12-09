import re
with open(0) as f:
    lines = f.readlines()

seeds = lines[0].split(':')[1].strip().split(' ')
seeds = [int(s) for s in seeds]
print(seeds)

maps = []

for line in lines[1:]:
    if line == '\n':
        maps.append([])
    numbers = re.findall('\d+', line)
    if len(numbers) > 0:
        maps[len(maps)-1].append(list(map(int, numbers)))

def get_next(m, n):
    for dest, source, l in m:
        if (source<= n) and (n < source + l):
            return dest + n - source
    else:
        return n

cu = seeds
for m in maps:
    next = []
    for s in cu:
        next.append(get_next(m, s))
    cu = next
#print(cu)
print(min(cu))