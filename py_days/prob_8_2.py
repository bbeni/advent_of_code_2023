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

''' brute force alert '''

starts = [k for k in mappings.keys() if k[-1] == "A"]
last_round = starts.copy()

instr_cycle_length = len(instructions)
instructions_index = [0 if instruction == "L" else 1 for instruction in instructions]

i = 0
for instruction_i in cycle(instructions_index):
    reached = 0
    next_round = []
    for last in last_round:
        next = mappings[last][instruction_i]
        next_round.append(next)

        if next[-1] == 'Z':
            reached += 1
    last_round = next_round
    i += 1
    if i%(instr_cycle_length*100000)==0:
        print(i/52766656211*100)
        print(last_round, i)
    if reached == len(starts):
        break

print(last_round, i)


# > 52766656211
#print("\033[92mEZCLAP\033[0m")