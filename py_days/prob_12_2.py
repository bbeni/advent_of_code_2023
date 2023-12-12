import math

def linear_count(seq, block):
    s = 0
    for i in range(0, len(seq)-block+1):
        if (not '.' in seq[i:i+block]) and (not '#' in seq[:i]+seq[i+block:]) :
            s += 1
    return s

def partition_count(seq, counts):
    if sum(counts) + len(counts) - 1 > len(seq):
        return 0
    if counts == []:
        return 1
    if len(counts) == 1:
        l = linear_count(seq, counts[0])
        return l
    if len(counts) == 2:
        first_block = counts[0]
        second_block = counts[1]
        t = 0
        for i in range(0, len(seq)-first_block-second_block):
            if (not '.' in seq[i:i+first_block]) and (not '#' in seq[:i]+seq[i+first_block]):
                t += linear_count(seq[i+first_block+1:], second_block)
        return t

    mid = math.floor(len(counts)/2)
    mid_block = counts[mid]
    start = len(counts[:mid]) + sum(counts[:mid])
    end = len(seq) - len(counts[mid+1:]) - sum(counts[mid+1:]) - mid_block +1

    s = 0
    for i in range(start, end):
        if not( '.' in seq[i:i+mid_block]) and not ('#' in seq[i-1]+seq[i+mid_block]):
            left = partition_count(seq[:i-1], counts[:mid])
            right = partition_count(seq[i+mid_block+1:], counts[mid+1:])
            s += left*right
    return s


with open(0) as f:
    lines = f.readlines()

s = 0
for i, l in enumerate(lines):
    a, b = l.split(' ')
    b = b.strip()
    b = (5*(b+','))[:-1]
    counts = list(map(int, b.strip().split(',')))
    seq = (5*(a+'?'))[:-1]
    t = partition_count(seq, counts)
    #print('got count:', t)
    s += t

print(s)

# too high 14071588376276841
# too low      9114117623639
# wrong        9114117628619
# wrong       26727076155415