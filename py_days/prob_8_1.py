


mappings = {}


for i,  l in enumerate(open(0)):
    l = l.strip()
    if (i == 0):
        instructions = 100*l
        #print(instructions)
        continue
    if (l == ""):
        continue
    
    start = l.split(" = ")[0]
    options = l.split(" = ")[1][1:-1].split(', ')
    mappings[start] = options


#print(mappings)

final = "AAA"
i = 0
while (final != "ZZZ"):
    index = 0 if instructions[i] == "L" else 1
    final = mappings[final][index]
    #print(final)
    i += 1
print(i)


#print("\033[92mEZCLAP\033[0m")