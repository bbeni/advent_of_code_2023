'''
notes:
======
only works for small input sizes
need a better idea

'''
from collections import defaultdict
from heapq import heapify, heappop, heappush
from itertools import product

def dijkstra(nodes: list, edges: dict, sources:list):
    '''start at source and compute all minimal distances
        uses the priority queue from
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    '''
    visited = set()
    # some large number
    distances = defaultdict(lambda: 2**59)
    prev = {}

    # priority queue
    Q = []
    for source in sources:
        distances[source] = 0
        Q.append((0, source))
        prev[source] = source
    heapify(Q)

    while Q != []:
        _, current_node = heappop(Q)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for node, weight in edges[current_node]:
            if node in visited:
                continue
            new_dist = distances[current_node] + weight
            if new_dist < distances[node]:
                distances[node] = new_dist
                heappush(Q, (new_dist, node))
                prev[node] = current_node

    return distances, prev

def create_graph():
    nodes = []
    for from_vertical in [True, False]:
        for i, j in product(range(WIDTH), range(WIDTH)):
            nodes.append((i, j, from_vertical))
    edges = defaultdict(list)
    for node in nodes:
        i, j, from_vertical = node
        for offset in [10,9,8,7,6,5,4,-10,-9,-8,-7,-6,-5,-4]:
            s = 1 if offset > 0 else -1
            if from_vertical:
                # connect horizontal
                if i+offset < 0 or i+offset >= WIDTH:
                    continue
                w = sum([grid[i+o][j] for o in range(s, offset+s, s)])
                edges[node].append(((i+offset, j, False), w))
            else:
                # connect vertical
                if j+offset < 0 or j+offset >= WIDTH:
                    continue
                w = sum([grid[i][j+o] for o in range(s, offset+s, s)])
                edges[node].append(((i, j+offset, True), w))
    
    
    nodes.insert(0, 'start')
    nodes.append('end')
    edges['start'] = [
        ((0, 0, True), 0),
        ((0, 0, False), 0)
    ]
    edges[(WIDTH-1, WIDTH-1, True)].append(('end', 0))
    edges[(WIDTH-1, WIDTH-1, False)].append(('end', 0))

    return nodes, edges


lines = [line.strip() for line in open(0).readlines()]
grid = [list(map(int, line)) for line in lines]
WIDTH = len(grid)

nodes, edges = create_graph()
dist, path = dijkstra(nodes, edges, ['start'])
print(dist['end'])