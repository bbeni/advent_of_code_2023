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

print(mappings)

starts = [k for k in mappings.keys() if k[-1] == "A"]



finals = starts
print(finals)
n = []



so_fars = []

for final in finals:
    i = 0

    so_far = []
    goals = []
    cycles = []
    for instruction in cycle(instructions):
        index = 0 if instruction == "L" else 1
        final = mappings[final][index]


        i += 1
        if final[-1] == 'Z':
            goal = i
            goals.append(i)
            #print(i)
        # cycle

        if final in so_far:
            length = so_far[::-1].index(final)+1
            #print(length)
            if length % len(instructions) == 0:
                print('cycle length divisible by instr_length')
                print(len(so_far), goals, i)
                break


        
        #if final in so_far:
        #    so_far.append(final)
        #    break
        so_far.append(final)

    so_fars.append(so_far)




# > 52766656211
#print("\033[92mEZCLAP\033[0m")