# 백준 17396: 백도어

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0))

    while queue:
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist:
            continue

        for next, d in graph[cur]:
            cost = d + dist
            # 최단 거리 & 상대방 시야에 보이지 않는 곳
            if cost < distance[next] and view[next] == 0:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))

n, m = map(int, input().split())

view = list(map(int, input().split()))
view[-1] = 0 # 상대편 넥서스가 있는 곳

graph = [[] for _ in range(n)]
distance = [float('INF')] * n

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

dijkstra()

if distance[-1] < float('INF'):
    print(distance[-1])
else:
    print(-1)