import re

workflows = {}
parts = []

wf_read = True
for line in open(0):
    if line.strip() == '':
        wf_read = False
        continue

    if wf_read:
        id, rest = line.strip().split('{')
        conds = []
        for cond in rest.strip('}').split(','):
            if ':' in cond:
                c, to =cond.split(':')
            else:
                c, to = 'True', cond
            conds.append((c, to))
        workflows[id] = conds
    else:
        parts.append(list(map(int, re.findall(r'\d+', line.strip()))))


total = 0
for part in parts:
    current = 'in'
    x, m, a, s = part
    while True:
        if current == 'A':
            total += x+m+a+s
            break
        if current == 'R':
            break
        wf = workflows[current]
        for cond, res in wf:
            if eval(cond):
                current = res
                break

print(total)