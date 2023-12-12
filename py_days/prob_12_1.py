with open(0) as f:
    lines = f.readlines()

def possible(sequence):
    if len(sequence) <= 0:
        yield []

    for p in possible(sequence[1:]):
        if len(sequence) == 0:
            break
        if sequence[0] == '?':
            yield ['.'] + p
            yield ['#'] + p
        else:
            yield [sequence[0]] + p

def count(sequence):
    count = 0
    coll = []
    for x in sequence:
        if x == '#':
            count+=1
        elif count != 0:
            coll.append(count)
            count = 0
    if count != 0:
        coll.append(count)
    return coll


s = 0
for l in lines:
    a, b = l.split(' ')
    c = list(map(int,b.split(',')))
    seq = list(a)
    #print(seq)
    for p in list(possible(seq)):
        if (c == count(p)):
            s += 1


print(s)
