# 백준 1916: 최소비용 구하기

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for g in graph[now]:
            cost = dist + g[1]

            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(queue, (cost, g[0]))

n = int(input())
graph = [[] for _ in range(n+1)]
distance = [float('INF')] * (n+1)

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])
