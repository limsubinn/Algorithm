import sys
import heapq

def input():
    return sys.stdin.readline().strip()

v, e = map(int, input().split())

graph = [[] for _ in range(v)] # 노드 연결 정보
distance = [[float('INF')] * v for _ in range(v)] # 최단 거리
heap = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    heapq.heappush(heap, [c, a-1, b-1])

answer = -1
while heap:
    c, a, b = heapq.heappop(heap)

    # 출발지 == 도착지 : 사이클
    # 힙 -> 최소 비용부터 나온다.
    if a == b:
        answer = c
        break

    if distance[a][b] < c:
        continue

    for node, cost in graph[b]:
        cost += c
        # 최솟값 갱신
        if cost < distance[a][node]:
            distance[a][node] = cost
            heapq.heappush(heap, [cost, a, node])

print(answer)

'''
플로이드 워셜 - python3 시간 초과 / pypy3 940ms

import sys

def input():
    return sys.stdin.readline().strip()

v, e = map(int, input().split())

graph = [[float('INF')] * v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = float('INF')
for i in range(v):
    if graph[i][i] < answer:
        answer = graph[i][i]

if answer != float('INF'):
    print(answer)
else:
    print(-1)
'''