import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[b] = parent[a]
        result[a] += result[b]

t = int(input())

for i in range(t):
    f = int(input())
    parent = dict()
    result = dict()

    for j in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            result[a] = 1

        if b not in parent:
            parent[b] = b
            result[b] = 1

        union_parent(a, b)
        print(result[find_parent(a)])