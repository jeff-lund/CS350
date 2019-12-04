from sys import argv
import random
import graph # copied over froms CS350/Prims/

def dfs(g):
    g2 = list(g)
    visited = set()
    processing = [g2[0][0]]
    processed = []

    while len(processing):
        s = processing.pop()
        if s not in visited:
            processed.append(s)
            visited.add(s)
        for u, v, _ in g2:
            if u == s and v not in visited:
                processing.append(v)
            elif v == s and u not in visited:
                processing.append(u)
    return processed
    
def twice_around(g):
    mst = g.prims()
    walk = dfs(mst)
    seen = set()
    rwalk = []
    for v in walk:
        if v not in rwalk:
            rwalk.append(v)
    tour = []
    i = 0
    while i < len(rwalk) - 1:
        v1 = rwalk[i]
        v2 = rwalk[i + 1]
        for a, b, w in g.edges:
            if a == v1 and b == v2 or a == v2 and b == v1:
                tour.append((v1, v2, w))
                break
        i += 1
    return tour

if __name__ == '__main__':
    n = int(argv[1])
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            w = random.randint(1, 20)
            e = (i, j, w)
            ee = (j, i, w)
            edges.append(e)
            edges.append(ee)
    g = graph.GraphEL(n, edges)
    #print(g)
    print("Finding tour")
    tour = twice_around(g)
    print("Tour found")
    tweight = 0
    for e in tour:
        print(e)
        tweight += e[2]
    print("Total length of tour:", tweight)
