import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

# 최단 경로 테이블
graph = [[float('INF')] * (n+1) for _ in range(n+1)]
# 경로표
result = [['-'] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 최단 경로 테이블 갱신
    graph[a][b] = c
    graph[b][a] = c
    # 경로표 갱신
    result[a][b] = b
    result[b][a] = a

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 최단 경로 테이블, 경로표 갱신
            if graph[i][j] > graph[i][k] + graph[k][j] and i != j:
                graph[i][j] = graph[i][k] + graph[k][j]
                result[i][j] = result[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(result[i][j], end=' ')
    print()