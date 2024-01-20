# 백준 20040: 사이클 게임

import sys

def input():
    return sys.stdin.readline().strip()

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n)]

answer = 0
for i in range(1, m+1):
    a, b = map(int, input().split())

    # 사이클 발생
    if find(a) == find(b):
        answer = i
        break

    # 연결
    union(a, b)

print(answer)
