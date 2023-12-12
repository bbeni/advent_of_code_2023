import math

def linear_count(seq, block):
    s = 0
    for i in range(len(seq)-block):
        if not ('.' in seq[i:i+block]):
            s += 1
    return s

def partition_count(seq, counts):
    print(seq, counts)
    if counts == []:
        return 1
    if len(counts) == 1:
        return linear_count(seq, counts[0])
    if sum(counts) + len(counts) - 1 > len(seq):
        return 0

    middle = math.ceil(len(seq)/2)
    s = 0
    for i in range(1, len(counts)):
        l = partition_count(seq[:middle], counts[:i])
        r = partition_count(seq[middle:], counts[i:])

        # check for overlap case from left
        x = counts[i-1]
        for offset in range(1, x):
            if (not '.' in seq[middle-offset:middle-offset+x]):
                lx = partition_count(seq[:middle-offset], counts[:i-1])
                rx = partition_count(seq[middle-offset+x:], counts[i:])
                #s += lx*rx

        # check for overlap case from right
        x = counts[i]
        for offset in range(1, x):
            if (not '.' in seq[middle-offset:middle-offset+x]):
                lx = partition_count(seq[:middle-offset], counts[:i])
                rx = partition_count(seq[middle-offset+x:], counts[i+1:])
                #s += lx*rx

        s += l*r
    return s


with open(0) as f:
    lines = f.readlines()

s = 0
for i, l in enumerate(lines[-1:]):
    a, b = l.split(' ')
    b = b.strip()
    b = (5*(b+','))[:-1]
    counts = list(map(int, b.strip().split(',')))
    seq = (5*(a+'?'))[:-1]
    print('starting', seq, counts)
    t = partition_count(seq, counts)
    print('got count:', t)
    s += t

print(s)

# too high 14071588376276841
# too low      9114117623639
# wrong        9114117628619
# wrong       26727076155415