import math
from sys import argv, exit
import argparse
from heap import Heap

class AdjVertex:
    '''
    Vertex of an adjacency list.
    Holds its label and a list of adjacent vertices in neighbors
    Each adjacent vertex is stored with (label, edge weight)
    '''
    def __init__(self, label):
        self.label = label
        self.neighbors = []

    def add_edge(self, label, weight):
        self.neighbors.append((label, weight))

class GraphAdj:
    def __init__(self, nvertices, edges):
        '''
        Creates an adjacency matrix from an edge list
        Uses a dictionary to hold each vertex.
        Key, value ==> label : AdjVertex object
        '''
        self.nvertices = nvertices
        self.vertices = {}
        for v1, v2, cost in edges:
            if v1 not in self.vertices.keys():
                self.vertices[v1] = AdjVertex(v1)
            self.vertices[v1].add_edge(v2, cost)

    def prims(self):
        '''
        Uses Prims algorithm to create a minimum spanning tree
        '''
        # Initialize set of tree vertices with first vertex
        init_vertex = list(self.vertices.keys())[0]
        tree_vertices = {init_vertex}
        # Create priority queue using min-heap with frontier from starting vertex
        pq = Heap()
        for lbl, wt in self.vertices[init_vertex].neighbors:
            pq.insert((init_vertex, lbl, wt))

        # set of the edges of the mst
        mst = set()

        while len(mst) != self.nvertices - 1:
            # find min weight edge
            u, v, w = pq.delete_min()
            # Because we reinsert edges with different priorities we need to make
            # sure that one of the vertices is not in the set, otherwise we would
            # add a cyclic edge.
            while u in tree_vertices and v in tree_vertices:
                u, v, w = pq.delete_min()
            # we want u to be the new vertex and v to be the vertex that was already
            # in the tree set so swap if necessary
            if u in tree_vertices:
                u, v = v, u
            # add u to Tree set
            tree_vertices.add(u)
            # expand frontier vertices from u, new vertex
            for lbl, wt in self.vertices[u].neighbors:
                if lbl not in tree_vertices:
                    pq.insert((u, lbl, wt))

            # add new edge to edge set
            mst.add((u, v, w))

        return mst

    def __repr__(self):
        ''' Representation of graph when used in print() statement '''
        ret = []
        for vertex in self.vertices:
            ret.append(vertex + ' [' + \
                    ', '.join(map(str, self.vertices[vertex].neighbors)) \
                    + ']')
        return '\n'.join(ret)

class GraphEL:
    '''
    Edge list representation of a graph
    The edges argument is a list of tuples (v1, v2, weight)
    Vertices are not explicitly maintained, only contained with the edge list
    '''
    def __init__(self, nvertices, edges):
        self.edges = edges
        self.nvertices = nvertices

    def convert_to_adj(self):
        return GraphAdj(self.nvertices, self.edges)

    def prims(self):
        mst = set()
        init_vertex = self.edges[0][0]
        tree_vertices = {init_vertex}
        while len(mst) != self.nvertices - 1:
            min_edge = None
            min_edge_weight = math.inf
            # find min weight edge u, v
            for u, v, w in self.edges:
                # only need to check one way as each edge is duplicated
                # would not work on directed graph
                if u in tree_vertices and v not in tree_vertices:
                    if w < min_edge_weight:
                        min_edge = (u, v, w)
                        min_edge_weight = w
            # add v to tree vertices
            tree_vertices.add(min_edge[1])
            # add edge to mst
            mst.add(min_edge)

        return mst

    def __repr__(self):
        return '\n'.join(map(str, self.edges))

def read_from_file(fname):
    '''
    Creates an edge list representation of a graph from a text file in the format
    <v1>, <v2>, <weight>
    Assumed to be an undirected graph so we add two edges for each line to represent
    v1 --> v2 and v2 --> v1
    '''
    edges = []
    with open(fname, 'r') as f:
        vertices = set()
        for line in f:
            # Splits the string into a list "x, y, 3" --> ['x', ' y', ' 3']
            v1, v2, weight = line.split(',')
            # Strips white space from the front and back of strings
            v1 = v1.strip()
            v2 = v2.strip()
            # convert weight into numeric value
            weight = float(weight)
            # append two tuples as the graph is undirected
            edges.append((v1, v2, weight))
            edges.append((v2, v1, weight))
            if v1 not in vertices:
                vertices.add(v1)
            if v2 not in vertices:
                vertices.add(v2)
    return GraphEL(len(vertices), edges)

if __name__ == '__main__':
    # Parsing command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--edgelist', action='store_true', 
            default=True, help='Use edge list representation')
    parser.add_argument('-a', '--adjlist', action='store_true', 
            default=False, help='Use adjacency list representation')
    parser.add_argument('-f', '--file', action='store', help='file to read graph from')
    args = parser.parse_args()

    # Create graph in desired form
    graph = read_from_file(args.file)
    if args.adjlist:
        graph = graph.convert_to_adj()
    
    # Get MST of input graph
    mst = graph.prims()
    total_weight = 0
    mst = list(mst)
    mst.sort(key=lambda x : x[2])
    for edge in mst:
        print(edge)
        total_weight += edge[2]
    print("Total weight of the tree:", total_weight)
