from copy import deepcopy
from math import prod

workflows = {}
parts = []

wf_read = True
for line in open(0):
    if line.strip() == '':
        break
    id, rest = line.strip().split('{')
    conds = []
    for cond in rest.strip('}').split(','):
        if ':' in cond:
            c, to =cond.split(':')
        else:
            c, to = 'True', cond
        conds.append((c, to))
    workflows[id] = conds

start = 'in'
possible_paths = []

def walk_paths(start, xmas=[[1,4000], [1,4000], [1,4000], [1,4000]]):
    xmas = deepcopy(xmas)

    if start == 'A':
        return prod([max(b-a+1, 0) for a, b in xmas])
    if start == 'R':
        return 0

    s = 0
    for cond, target in workflows[start]:    
        if cond == 'True':
            s += walk_paths(target, xmas)
            break

        xmas_follow = deepcopy(xmas)
        var, sign, n = cond[0], cond[1], int(cond[2:])
        var_index = 'xmas'.index(var)
        rng = xmas[var_index]
        rng_follow = xmas_follow[var_index]
        if sign == '>':
            rng[1] = min(rng[1], n)
            rng_follow[0] = max(rng_follow[0], n+1)
        else:
            rng[0] = max(rng[0], n)
            rng_follow[1] = min(rng_follow[1], n-1)


        s += walk_paths(target, xmas_follow)
    return s

print(walk_paths(start))