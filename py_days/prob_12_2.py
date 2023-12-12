


with open(0) as f:
    lines = f.readlines()

def perm_sums_up(n, length):
    if length == 0:
        return []
    if length == 1:
        yield [n]

    for i in range(0,n+1):
        for p in perm_sums_up(n-i, length-1):
            yield [i] + p


def generate_from_counts(counts, l):
    n_broken = sum(counts) 
    n_c = len(counts)-1
    # n_broken + n_c + n_sep = l
    # additional separators to place between
    n_sep = l - n_broken - n_c

    # arr [0, 0, 2, 2] len n_c

    results = []
    for arr in perm_sums_up(n_sep, n_c+2):
        results.append(make_seq(counts, arr))


    return results

def make_seq(counts, sep_arr):
    ### counts [1 2 3 1]
    ### sep_arr [0 0 1 2 2]
    ### -> '#.##..###...#..'
    res = sep_arr[0]*'.'
    for a, b in zip(counts[:-1], sep_arr[1:-1]):
        res += a*'#' + '.' + b*'.'
    return res + counts[-1]*'#' + sep_arr[-1]*'.'

def matches(a, b):
    #print(a)
    #print(b)
    for x, y in zip(a, b):
        #print(x, y)
        if (x == '#' and y == '.') or (x =='.' and y =='#'):
            return False
    return True


s = 0
for i, l in enumerate(lines):
    a, b = l.split(' ')
    b = b.strip()
    b = (b+',')[:-1]
    counts = list(map(int, b.strip().split(',')))
    
    seq = a
    
    q = 0
    matching = []
    for x in generate_from_counts(counts, len(seq)):
        if matches(x, seq):
            q+=1
            matching.append(x)


    
    seq = '?' + a + '?'
    t = 0
    matching = []
    for x in generate_from_counts(counts, len(seq)):
        if matches(x, seq):
            t+=1
            matching.append(x)

    seq = a + '?'
    t1 = 0
    matching = []
    for x in generate_from_counts(counts, len(seq)):
        if matches(x, seq):
            t1+=1
            matching.append(x)

    seq = '?' + a
    t2 = 0
    matching = []
    for x in generate_from_counts(counts, len(seq)):
        if matches(x, seq):
            t2+=1
            matching.append(x)

    if q == 1:
        t1, t2, t = 1, 1, 1
    print(t1*t2*t**3, t, t1, t2)
    s += t1*t2*t**3

print(s)

# too high 14071588376276841
# too low      9114117623639
# wrong        9114117628619
# wrong       26727076155415