from sys import argv
from union_find import UnionFind

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.cities = set()
        for u, v, _ in edges:
            self.cities.add(u)
            self.cities.add(v)

def kruskals(g):
    edges = sorted(g.edges, key=lambda e: e[2])
    u = UnionFind()
    # set up all the cities as trees in UF
    for city in g.cities:
        u.makeset(city)
    mst = []
    for e in edges:
        q, v, _ = e
        if u.find(q) != u.find(v):
            mst.append(e)
            u.union(q, v)
    return mst

def parse_file(fname):
    with open(fname, 'r') as f:
        raw = [line.strip().split(' ') for line in f]
        edges = [(u.strip(), v.strip(), float(w)) for u, v, w in raw]
    return edges

if __name__ == '__main__':
    fname = argv[1]
    g = Graph(parse_file(fname))
    mst = kruskals(g)
    total_weight = 0
    for e in mst:
        print(e)
        total_weight += e[2]
    print("total weight:", total_weight)
