from random import randint
from sys import argv

RED = '\033[1;31m'
RESET = '\033[0m'

def collect_litter(maze):
    nrow = len(maze)
    ncol = len(maze[0])
    dp = [[0 for _ in range(ncol)] for __ in range(nrow)]
    dp[0][0] = maze[0][0]
    # fill in the first row
    for j in range(1, ncol):
        dp[0][j] = dp[0][j - 1] + maze[0][j]
    
    for i in range(1, nrow):
        dp[i][0] = dp[i - 1][0] + maze[i][0]
        # for each spot find if the best result is from coming from the left or coming from the top
        for j in range(1, ncol):
            dp[i][j] = max(dp[i -1][j], dp[i][j - 1]) + maze[i][j]
    
    
    i = nrow - 1
    j = ncol - 1
    path = [(i, j)]
    while i != 0 and j != 0:
        if dp[i - 1][j] > dp[i][j - 1]:
            # came from the left
            i -= 1
        else:
            j -= 1
        path.append((i, j))
    while i != 0:
        i -= 1
        path.append((i, j))
    while j != 0:
        j -= 1
        path.append((i, j))
    path.reverse()
    
    for i, j in path:
        maze[i][j] = RED + str(maze[i][j]) + RESET
    for i in range(nrow):
        print(' '.join(map(str, maze[i])), '\t', dp[i])
    
    
    return dp[nrow - 1][ncol - 1]

maze = [[0,0,0,0,1,0],
        [0,1,0,1,0,0],
        [0,0,0,1,0,1],
        [0,0,1,0,0,1],
        [1,0,0,0,1,0]]
max_litter = collect_litter(maze)
print("maximum amount of litter that can be collected", max_litter)
