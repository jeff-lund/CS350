import random
from sys import argv

class Vertex:
    def __init__(self, animal):
        self.animal = animal
        self.edges = []

def dfs(V):
    stack = [0]
    processed = []
    marked = [False] * len(V)
    while stack:
        s = stack.pop()
        if not marked[s]:
            print(V[s].animal, "|", end=' ')
            marked[s] = True
        for v in V[s].edges:
            if not marked[v]:
                stack.append(v)
    print()

def bfs(V):
    marked = {V[0]}
    queue = [V[0]] # terrible queue, should use a real one
    dequeued = []
    while queue:
        vert = queue.pop(0)
        dequeued.append(vert)
        for w in vert.edges:
            if V[w] not in marked:
                marked.add(V[w])
                queue.append(V[w])
    for item in dequeued:
        print(item.animal, "| ", end='')
    print()




animals = ['whale', 'wolverine', 'quokka', 'wolf', 'bear', 'llama',
        'unicorn', 'eagle', 'falcon']
vertices = [Vertex(a) for a in animals]

do_dfs = argv[1] == 'dfs'
both = argv[1] == 'both'

n = len(vertices)
choices = [x for x in range(n)]

# Make weird graph
for v in vertices:
    r = random.randint(1, 3)
    v.edges = random.choices(choices, k=r)

# print starting graph
print("Our Graph")
for i, v in enumerate(vertices):
    print(i, v.animal)
    print(v.edges)

print('-' * 50)
if do_dfs or both:
    # DFS
    print("DFS")
    dfs(vertices)
if not dfs or both:
    print("BFS")
    bfs(vertices)
