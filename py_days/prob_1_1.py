import re 

s = 0
for line in open(0):
    x = re.findall(r'\d', line)
    a = int(x[0])
    b = int(x[::-1][0])
    s += a*10+b

print(s)