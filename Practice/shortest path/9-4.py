# 최단 경로 알고리즘
# 실전 문제1. 미래 도시

INF = int(1e9) # 무한

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 만들고 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받고, 서로에게 가는 비용을 1로 설정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이즘 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

dist = graph[1][k] + graph[k][x]

if dist >= INF:
    print("-1")
else:
    print(dist)