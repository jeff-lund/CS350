import sys
import math

def reconstruct_path(cameFrom, current):
    path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        path.append(current)
    return list(reversed(path))

def a_star(start, goal, graph, heuristic):
    '''
    start: starting city
    goal: ending city
    graph: currently edge list in list
    heuristic: 2-layer dictionary h[start][end] get heuristic from start to end
    Returns a list containing the path from start to end or None if no
    path exists
    '''
    all_cities = set()
    for c1, c2, weight in edge_list:
        all_cities.add(c1)
        all_cities.add(c2)
    if start not in all_cities or goal not in all_cities:
        return None, 0
    if start == goal:
        return [start], 0
    openSet = {start}
    cameFrom = dict()
    gScore = {city: math.inf for city in all_cities}
    gScore[start] = 0
    fScore = {city: math.inf for city in all_cities}
    fScore[start] = 0

    while openSet:
        current = min([(fScore[node], node) for node in openSet])[1]
        if current == goal:
            return reconstruct_path(cameFrom, current), gScore[current]
        openSet.remove(current)
        for cur, adj, cost in edge_list:
            # found an neighbor edge
            if cur == current or adj == current:
                # make sure cur is the current node and adj is the neighbor node
                if adj == current:
                    adj, cur = cur, adj
                # get a tenative score for the edge
                tenative = gScore[current] + cost
                # add/replace the neighbors values if we found a shorter path
                if tenative < gScore[adj]:
                    cameFrom[adj] = current
                    gScore[adj] = tenative
                    fScore[adj] = gScore[adj] + heuristic[adj][goal]
                    openSet.add(adj)
    return None, 0

if __name__ == '__main__':
    # Set up data structures
    graph_file = 'routes.txt'
    heur_file = 'euclidian.txt'
    with open(graph_file, 'r') as f:
        edge_list = []
        for line in f:
            # (Portland, Seattle, 174.3)\n 
            u, v, w = line.strip()[1:-1].split(',')
            # ["Portland", " Seattle", " 174.3"]
            edge_list.append( (u.strip(), v.strip(), float(w)) )

    with open(heur_file, 'r') as f:
        # heuristics is a 2-layer dictionary
        # first layer gets a dictionary of heuristics for the given
        # source city. second layer takes the goal city as a key
        # and retireves the euclidean distance from start to goal
        heuristics = dict()
        for line in f:
            start, end, val = line.strip().split(' ')
            val = float(val)
            if start not in heuristics:
                heuristics[start] = {}
            heuristics[start][end] = val
    start = sys.argv[1]
    goal = sys.argv[2]
    path, distance = a_star(start, goal, edge_list, heuristics)
    if path == None:
        print("Path does not exist between", start, "and", goal)
    else:
        print(' -> '.join(path))
        print("Total distance traveled:", distance)
