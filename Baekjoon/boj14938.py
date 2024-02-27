# 백준 14938: 서강그라운드

import sys

def input():
    return sys.stdin.readline().strip()

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

# 플로이드 워셜
graph = [[float('INF')] * n for _ in range(n)]
# 초기화
for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0
# 비용 입력
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l
# 최단 거리 갱신
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

answer = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        # 수색 범위 이내의 지역
        if graph[i][j] <= m:
            cnt += items[j]
    answer = max(answer, cnt)

print(answer)
