import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

planet = []
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    planet.append((i, x, y, z))

edges = []
for i in range(1, 4):
    planet.sort(key=lambda x: x[i])  # x값, y값, z값 기준 오름차순 정렬
    for j in range(n-1):
        edges.append((abs(planet[j+1][i]-planet[j][i]), planet[j][0], planet[j+1][0])) # 간선 정보 추가
edges.sort() # 비용 순으로 정렬

res = 0
for i in edges:
    c, a, b = i
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += c

print(res)