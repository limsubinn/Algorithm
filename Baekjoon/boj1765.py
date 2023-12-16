# 백준 1765: 닭싸움 팀 정하기

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
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]
enemies = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    r, p, q = input().split()
    p = int(p)
    q = int(q)
    # 친구 관계
    if r == 'F':
        union(p, q)
    # 원수 관계
    else:
        enemies[p].append(q)
        enemies[q].append(p)

# 원수의 원수는 친구
for enemy in enemies:
    if len(enemy) <= 1:
        continue
    e = enemy[0]
    for i in enemy[1:]:
        union(e, i)

for i in range(1, n+1):
    parent[i] = find(parent[i])

answer = len(set(parent[1:]))
print(answer)