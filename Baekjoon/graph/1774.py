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

n, m = map(int, input().split())

parent = [0] * (n+1) # 부모 노드 저장
for i in range(1, n+1):
    parent[i] = i

space = [0] # 우주신들의 좌표
for _ in range(n):
    x, y = map(int, input().split())
    space.append((x, y))

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

edges = [] # 모든 노드들의 간선
for i in range(1, n+1):
    for j in range(1, n+1):
        x1 = space[i][0]
        y1 = space[i][1]
        x2 = space[j][0]
        y2 = space[j][1]
        c = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
        edges.append((c, i, j))
edges.sort()

res = 0
for i in edges:
    c, a, b = i
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += c

print(f'{res:.2f}') # 소수점 둘째자리까지 출력
