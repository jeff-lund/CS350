from sys import argv

class Vertex:
    def __init__(self, value):
        self.val = value
        self.neighbors = []

    def __add__(self, v):
        self.neighbors.append(v)
    
    def __repr__(self):
        ret = str(self.val) + ' : '
        ret += ', '.join(map(str, map(lambda x: x.val, self.neighbors)))
        return ret

class Graph:
    ''' Adjacency List'''
    def __init__(self, edges):
        self.nvertices = 0
        self.vertices = []
        added = {}
        for u, v in edges:
            if u not in added:
                tmp = Vertex(u)
                self.vertices.append(tmp)
                added[u] = tmp
            if v not in added:
                tmp = Vertex(v)
                self.vertices.append(tmp)
                added[v] = tmp
            added[u] + added[v]
        self.nvertices = len(self.vertices)

    def __repr__(self):
        ret = ''
        for v in self.vertices:
            ret += str(v) + '\n'
        return ret

visited = set()
walk = []

def dfs_helper(g, v):
    global visited
    global walk
    visited.add(v)
    for n in v.neighbors:
        if n not in visited:
            dfs_helper(g, n)
    walk.append(v.val)

def dfs(g):
    global visited
    global walk
    visited.clear()
    walk.clear()
    for v in g.vertices:
        if v not in visited:
            dfs_helper(g, v)
    walk.reverse()
    return walk

def kahns(g):
    ''' Source removal algorithm '''
    # Holds the in-degree for each vertex
    counts = {}
    for v in g.vertices:
        counts[v] = 0
    for v in g.vertices:
        for n in v.neighbors:
            counts[n] += 1
    walk = []
    while len(walk) != g.nvertices:
        for v, c in counts.items():
            if c == 0:
                walk.append(v.val)
                counts[v] = -1
                for n in v.neighbors:
                    counts[n] -= 1
    return walk

if __name__ == '__main__':
    fname = argv[1]
    with open(fname, 'r') as f:
        edges = [line.strip().split(' ') for line in f]
    g = Graph(edges)
    print("Working Graph")
    print(g)
    w = dfs(g)
    print('-' * 50)
    print("Toposort from DFS")
    print(' '.join(walk))
    print('-' * 50)
    print('Toposort from source removal (kahns algorithm)')
    print(' '.join(kahns(g)))
