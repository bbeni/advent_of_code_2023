from itertools import permutations, tee
import functools


def memoized_generator(f):
    cache = {}
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        k = args, frozenset(kwargs.items())
        it = cache[k] if k in cache else f(*args, **kwargs)
        cache[k], result = tee(it)
        return result
    return wrapper


with open(0) as f:
    lines = f.readlines()


@memoized_generator
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
        res = ''
        for i, sep in zip(range(0, n_c), arr):
            res += sep*'.'  + counts[i]*'#' + '.'
        res += arr[-2]*'.' + counts[n_c]*'#' + arr[-1]*'.'
        results.append(res)

    return results

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
    a = 5*a
    b = b.strip()
    b = (5*(b+','))[:-1]
    counts = list(map(int, b.strip().split(',')))
    seq = a.strip().strip('.')
    print(seq)
    print(counts)    
    t = 0
    for x in generate_from_counts(counts, len(seq)):
        if matches(x, seq):
            t+=1

    #print(t, s)
    s += t

print(s)
