# 백준 10282: 해킹

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, c))

    while queue:
        c_dist, cur = heapq.heappop(queue)

        if distance[cur] < c_dist:
            continue

        for next, n_dist in graph[cur]:
            if c_dist + n_dist < distance[next]:
                distance[next] = c_dist + n_dist
                heapq.heappush(queue, (c_dist + n_dist, next))

MAX_VALUE = float('INF')

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [MAX_VALUE] * (n + 1)
    distance[c] = 0

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra()

    cnt, time = 0, 0 # 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
    for i in range(1, n+1):
        if distance[i] < MAX_VALUE:
            cnt += 1
            time = max(time, distance[i])

    print(cnt, time)
