'''
Solves the hiking problem part 2 of day 23.

Authors:
    NardoUzmaky     https://github.com/NardoUzmaky 
    bbeni           https://github.com/bbeni

'''

UNENDLICH = 230123012

grid = []
for line in open(0):
    grid.append(line.strip()
                .replace('>', '.')
                .replace('<', '.')
                .replace('^', '.')
                .replace('v', '.'))

width, height = len(grid[0]), len(grid)

class Node():
    def __init__(self, index):
        self.index = index
        self.connections = {}

    def add_connection(self, index, weight):
        self.connections[index] = weight

    def n_connections(self):
        return len(self.connections)

    def __repr__(self) -> str:
        return f"Node: {self.index} - {self.connections}"

def create_list_of_nodes(nodes, edges, weights):  
    nodes_list = []
    for i in range(len(nodes)):
        nodes_list.append(Node(i))
    for edge, weight in zip(edges, weights):
        nodes_list[edge[0]].add_connection(edge[1], weight)
        nodes_list[edge[1]].add_connection(edge[0], weight)
    return nodes_list


def get_legal_neigbours(coord):
    neighbours = []
    for neighbouring in ((coord[0]+1, coord[1]),
                        (coord[0]-1, coord[1]),
                        (coord[0], coord[1]+1),
                        (coord[0], coord[1]-1)):
    
        if not (0 <= neighbouring[0] < height and 0 <= neighbouring[1] < width):
            continue
        tile = grid[neighbouring[0]][neighbouring[1]]
        if tile == '#':
            continue
        neighbours.append(neighbouring)
    return neighbours

def length_to_next_node(start, previous):
        next = start
        for i in range(1,10000):
            neigbours = get_legal_neigbours(next)
            neigbours.remove(previous) # delete where we came from
            if len(neigbours)<1:
                return -1, next
            if len(neigbours) >1:
                return i, next
            # only one found
            previous = next
            next = neigbours[0]
        raise Exception('length_to_next().. exceeded')

def construct_graph():

    nodes = []
    for i in range(height):
        for j in range(width):
            neighbours = get_legal_neigbours((i,j))
            if len(neighbours) > 2 and grid[i][j] != '#':
                nodes.append((i,j))

    edges = []
    edge_weights = []
    for current_coord in nodes:
        neighbours = get_legal_neigbours(current_coord)
        if len(neighbours) > 2:
            for nb in neighbours:
                length, connected_node = length_to_next_node(nb, current_coord)
                if length == -1:
                    continue
                connected_idx = nodes.index(connected_node)
                this_idx = nodes.index(current_coord)
                if (connected_idx, this_idx) in edges:
                    continue
                edges.append((this_idx, connected_idx))
                edge_weights.append(length)

    return nodes, edges, edge_weights

def debug_print(coord=None, around=None):

    t, b, l, r = 0, None, 0, None
    if coord and around:
        i, j = coord[0], coord[1]
        t, b = i-around, i+1+around
        l, r = j-around, j+1+around
    
    for y, line in enumerate(grid[t:b]):
        if coord and coord[0]==y:
            print(line[:coord[1]] + 'X' + line[coord[1]+1:])
            continue
        print(line[l:r])
    print()


def fill_path(nodes_list):

    se = [node.index for node in nodes_list if node.n_connections() == 2]
    start = se[0]
    end = se[1]
    path = [start]
    def walk_path(path_length):
        current_index = path[-1]
        lens = []
        for next_node in nodes_list[current_index].connections.keys():
            if next_node in path:
                continue
            path.append(next_node)
            lens.append(walk_path(path_length+nodes_list[current_index].connections[next_node]))
            path.pop()
        if len(lens) == 0 and current_index == end:
            #print("found path: ", path_length)
            return path_length
        if len(lens) == 0:
            return -UNENDLICH
        return max(lens)
        
    length = walk_path(0)
    return length


nodes, edges, edge_weights = construct_graph()

nodes_list = create_list_of_nodes(nodes, edges, edge_weights)

#print(nodes_list)
first_length = length_to_next_node((1,1), (0,1))[0]
last_length = length_to_next_node((height-2,width-2), (height-1,width-2))[0]

length = fill_path(nodes_list)
print(length+first_length+last_length)