import sys

def input():
    return sys.stdin.readline().strip()

def commands(c, trains):
    if c[0] == 1:
        trains[c[1]-1][c[2]-1] = True
    elif c[0] == 2:
        trains[c[1]-1][c[2]-1] = False
    elif c[0] == 3:
        trains[c[1]-1] = [False] + trains[c[1]-1][:19]
    else:
        trains[c[1]-1] = trains[c[1]-1][1:] + [False]

n, m = map(int, input().split())
trains = [[False] * 20 for _ in range(n)]

for i in range(m):
    c = list(map(int, input().split()))
    commands(c, trains)

trains = list(map(tuple, trains))
answer = len(set(trains))
print(answer)