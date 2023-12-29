from turtle import color
import matplotlib.pyplot as plt
from random import randint
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


def check_part(part):
    current = 'in'
    x, m, a, s = part
    n = 0
    while True:
        n += 1
        if current == 'A':
            break
        if current == 'R':
            break
        wf = workflows[current]
        for cond, res in wf:
            if eval(cond):
                current = res
                break
    return current, n










def make_funny_mation():
#    for f in range(1, 4001, 8):
#        frame_nr = int((f-1)/8+1)
    for f in range(1,4001,14):
        frame_nr = int(f/14)+1 
        #make_funny_mation_frame(f, n_points=16000)
        make_funny_mation_frame(f, step=193)
        plt.savefig(f'funny_mation_21/frames/frame{str(frame_nr).rjust(4,"0")}.png')
        print(f'frame {frame_nr} of {4000}')
        plt.close()


def make_funny_mation_frame(f, step=133, show=False):
    rejects = []
    accepts = []
    for x in range(1,4001,step):
        for m in range(1,4001,step):
            for a in range(1,4001,step):
#    for i in range(n_points):
        #x,m,a,s = randint(1,4000),randint(1,4000),randint(1,4000),randint(1,4000)
                res,n = check_part((x,m,a,f))
                if res == 'A':
                    accepts.append((x,m,a,f))
                else:
                    rejects.append((x,m,a,f))

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')

    x = [r[0] for r in accepts]
    y = [r[1] for r in accepts]
    z = [r[2] for r in accepts]
    ax.scatter(x, y, z, marker='o', color='green', alpha=0.55)

    x = [r[0] for r in rejects]
    y = [r[1] for r in rejects]
    z = [r[2] for r in rejects]
    ax.scatter(x, y, z, color='magenta', alpha=0.55)

    ax.view_init(elev=f/93, azim=f/20)

    if show:
        plt.show()
    
#make_funny_mation_frame(2000, step=193, show=True)

#make_funny_mation()


'''
for i in range(1, 400100):
    x, n = check_part((random.randint(1,4000), random.randint(1,4000), random.randint(1,4000), random.randint(1,4000)))
    ns.append(n)

print(ns[:10], sum(ns)/len(ns))
print(max(ns))

max nr workflows per part for 400000 random samples: 8
average workflows: 3.5
'''