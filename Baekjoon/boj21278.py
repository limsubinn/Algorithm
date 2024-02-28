# 백준 21278: 호석이 두 마리 치킨

import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

graph = [[float('INF')] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    # 자기 자신으로 가는 경로 초기화
    graph[a][a] = 0

for _ in range(m):
    # 서로 연결되어 있는 경로
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 모든 그래프의 최단 거리 갱신
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

answer = float('INF')
for i in range(1, n): # 치킨집 1
    for j in range(i+1, n+1): # 치킨집 2
        result = 0
        # 모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간 구하기
        for k in range(1, n + 1):
            result += min(graph[i][k], graph[j][k])
        # 정답 갱신
        if result < answer:
            answer = result
            a, b = i, j

print(a, b, 2 * answer)
