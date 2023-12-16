with open(0) as f:
    lines = f.readlines()
    input = [line.strip() for line in lines][0]
    seq = input.split(',')
    operations = [s.split('=') if '=' in s else [s[:-1],0] for s in seq]
    
def hash(string):
    v = 0
    for i in range(len(string)):
        v += ord(string[i])
        v *= 17
        v %= 256
    return v

boxes = [ [] for _ in range(256) ]

for label, focal in operations:
    box_id = hash(label)
    # remove case
    if focal == 0:
        for i, x in enumerate(boxes[box_id]):
            l, f = x
            if l == label:
                del boxes[box_id][i]
                break
    else:
        removed = False
        for i, x in enumerate(boxes[box_id]):
            l, f = x
            if l == label:
                boxes[box_id][i] = [label, focal]
                removed = True
                break
        if not removed:
            boxes[box_id].append([label, focal])

s = 0
for j, b in enumerate(boxes):
    for i, x in enumerate(b):
        s += (j+1)*(i+1)*int(x[1])

print(s)