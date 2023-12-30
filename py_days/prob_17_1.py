'''
notes:
======

NxN
-path never intersects itself (every node only once)
-path has a smaller or equal energy value than any trivial path
-touching:
    when corner touching possible?
-edge only 1 to 9 values
-if we know path length l and ignore length 3 constraint: 
    l = 2N-1 case:
        2^l = 2^(2N-1) possible paths -> not even that is brutforcible
        but we could go through all contra diagonal elements and
        reduce the problem to 2*(1 + (N-1) + (N-2)(N-3)/2 + ..) < N*2^(N+1)
        (might be very wrong haha)

        funny: add m_(i-1)i += m_ii m_i(i-1) += m_ii until contra diagonal
        from m_00 too until contra diagonal.. ok wrong but maybe idea

        better: for every contra diagonal n m_ab += min(m(a+1)b, m(a)(b+1))

    l > 2N-1 case:
        o = (l - (2N-1))/2 is the number backwards going paths 
        (negative indices change)
        note: some diagonals get crossed additionally in total 2*o times.
        


ideas:
======
flood fill with delay
lagrange multipliers
monte carlo
simulated annealing
a*
dykstra
diagonalize?

        
'''
import numpy as np
from scipy.sparse import coo_array

lines = [line.strip() for line in open(0).readlines()]

grid = [list(map(int, line)) for line in lines]
grid = np.array(grid)
print(grid)

def build_adjacency(grid):
    N = grid.shape[0]*grid.shape[1]
    row = []
    col = []
    data = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            this = i+j*grid.shape[0]
            for k, l in [(i, j-1), (i, j+1), (i-1, j), (i+1,j)]:
                if k < 0 or l < 0 or k >= grid.shape[0] or l >= grid.shape[1]:
                    continue
                index = k+l*grid.shape[0]
                row.extend([this, index])
                col.extend([index, this])
                data.extend([grid[i][j], grid[i][j]])
    A = coo_array((data,(row, col))).todia()
    return A

N = grid.shape[0]*grid.shape[1]
A = build_adjacency(grid)


distance = np.zeros((N,))
distance[:] = np.inf
distance[0] = 0

previous = []

print(distance)

def dykstra(A, start=0):
    pass



#print(A)


# 1245 too high