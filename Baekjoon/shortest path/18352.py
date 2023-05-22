import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, x))
    distance[x] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i, c in graph[now]:
            cost = dist + c

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(queue, (cost, i))

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [float('INF')] * (n+1)
dijkstra()

result = []
for i in range(n+1):
    if distance[i] == k:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)