from itertools import cycle
import math

mappings = {}

for i,  l in enumerate(open(0)):
    l = l.strip()
    if (i == 0):
        instructions = l
        #print(instructions)
        continue
    if (l == ""):
        continue
    
    start = l.split(" = ")[0]
    options = l.split(" = ")[1][1:-1].split(', ')
    mappings[start] = options



starts = [k for k in mappings.keys() if k[-1] == "A"]
last_round = starts.copy()

instr_cycle_length = len(instructions)
instructions_index = [0 if instruction == "L" else 1 for instruction in instructions]

cycles = []
for last in last_round:

    i = 0
    hits = []
    for instruction_i in cycle(instructions_index):
        next = mappings[last][instruction_i]
        i += 1
        if next[-1] == 'Z':
            exit=False
            for h in hits:
                if (i - h) % instr_cycle_length == 0:
                    exit = True
            hits.append(i)
            if exit:
                break

        last=next
    
    cyc = (h ,i-h)
    cycles.append(cyc)


r = math.lcm(*[x[1] for x in cycles])
print(r)


# > 52766656211
#   14299763833181
#print("\033[92mEZCLAP\033[0m")