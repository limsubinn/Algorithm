import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    distance = [float('INF')] * n
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for g, c in graph[now]:
            cost = dist + c
            if cost < distance[g]:
                distance[g] = cost
                heapq.heappush(heap, (cost, g))

    return distance

n = int(input())
a, b, c = map(int, input().split())

graph = [[] for _ in range(n)]

m = int(input())
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d-1].append((e-1, l))
    graph[e-1].append((d-1, l))

# A, B, C에서 출발한 다익스트라 수행
d1 = dijkstra(a-1)
d2 = dijkstra(b-1)
d3 = dijkstra(c-1)

result = 0 # 가장 거리가 먼 곳
answer = 0
for i in range(n):
    temp = min(d1[i], d2[i], d3[i]) # 가장 거리가 가까운 곳
    if result < temp: # 최댓값 갱신
        result = temp
        answer = i+1

print(answer)