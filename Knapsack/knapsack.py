import random
from sys import argv

WAIT = False
memo = []
call_count = 0
hit_count = 0

def memo_printer():
    global memo
    print("-" * 80)
    for line in memo:
        print('\t'.join(map(str, line)))

def memo_sack(W, V, C, i, j):
    global memo
    global call_count
    global hit_count
    call_count += 1
    if memo[i][j] == None:
        if W[i - 1] > j:
            memo[i][j] = memo_sack(W, V, C, i - 1, j)
        else:
            a = memo_sack(W, V, C, i - 1, j)
            b = memo_sack(W, V, C, i - 1, j - W[i - 1]) + V[i - 1]
            memo[i][j] = max(a, b)
    else:
        hit_count += 1
    if WAIT:
        memo_printer()
        input()
    return memo[i][j]


C = 20
n = 10
V = [random.randint(1, 200) for _ in range(n)]
W = [random.randint(1, 30) for _ in range(n)]
print(V)
print(W)
input()
memo = [[None for _ in range(C + 1)] for __ in range(n + 1)]
for i in range(C + 1):
    memo[0][i] = 0
memo_sack(W, V, C, n, C)
memo_printer()
print("total calls:", call_count)
print("looks up found:", hit_count)
