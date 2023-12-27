'''
Authors:
    https://github.com/NardoUzmaky
    https://github.com/bbeni

'''

import sympy 

coords = []
velocities = []
for line in open(0):
    a, b = line.strip().split('@')
    coords.append(tuple(map(int,a.split(', '))))
    velocities.append(tuple(map(int,b.split(', '))))

def solve_equations(pos1, vel1, pos2, vel2, pos3, vel3):
    x0, y0, z0, u0, v0, w0, t1, t2, t3 = sympy.symbols('x0 y0 z0 u0 v0 w0 t1 t2 t3')
    eq1 = sympy.Eq(pos1[0] + t1*vel1[0],  x0 + t1*u0)
    eq2 = sympy.Eq(pos1[1] + t1*vel1[1],  y0 + t1*v0)
    eq3 = sympy.Eq(pos1[2] + t1*vel1[2],  z0 + t1*w0)
    eq4 = sympy.Eq(pos2[0] + t2*vel2[0],  x0 + t2*u0)
    eq5 = sympy.Eq(pos2[1] + t2*vel2[1],  y0 + t2*v0)
    eq6 = sympy.Eq(pos2[2] + t2*vel2[2],  z0 + t2*w0)
    eq7 = sympy.Eq(pos3[0] + t3*vel3[0],  x0 + t3*u0)
    eq8 = sympy.Eq(pos3[1] + t3*vel3[1],  y0 + t3*v0)
    eq9 = sympy.Eq(pos3[2] + t3*vel3[2],  z0 + t3*w0)
    solution = sympy.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (x0, y0, z0, u0, v0, w0, t1, t2, t3))
    solution = sum((solution[0][:3]))
    print(solution)

solve_equations(coords[0], velocities[0], coords[1], velocities[1], coords[2], velocities[2])