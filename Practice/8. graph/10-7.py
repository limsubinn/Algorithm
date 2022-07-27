# 그래프 이론
# 실전 문제2. 도시 분할 계획

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
biggest = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c # 최종 결과에 비용 더하기
        biggest = c # 비용 순으로 정렬했기 때문에 현재의 비용이 가장 큰 비용

print(result - biggest) # 최종 결과에서 가장 큰 비용 뺴기