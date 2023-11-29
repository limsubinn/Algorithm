import sys

def input():
    return sys.stdin.readline().strip()

def command(a, b, c, bulbs):
    if a == 1:
        bulbs[b-1] = c
        return
    if a == 2:
        for i in range(b-1, c):
            if bulbs[i] == 0: bulbs[i] = 1
            else: bulbs[i] = 0
        return
    if a == 3:
        for i in range(b-1, c):
            bulbs[i] = 0
        return
    for i in range(b-1, c):
        bulbs[i] = 1

n, m = map(int, input().split())
bulbs = list(map(int, input().split()))

for i in range(m):
    a, b, c = map(int, input().split())
    command(a, b, c, bulbs)

for i in bulbs:
    print(i, end=' ')