import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def dijkstra(start):
    distance = [float('INF')] * (n+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for g, c in graph[now]:
            cost = dist + c
            if cost < distance[g]:
                distance[g] = cost
                heapq.heappush(heap, [cost, g])

    return distance

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

answer = 0
for i in range(1, n+1):
    # (i -> x) + (x -> i)의 최댓값
    answer = max(answer, dijkstra(i)[x] + dijkstra(x)[i])

print(answer)
