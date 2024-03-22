# 프로그래머스 12978: 배달

import heapq

def dijkstra(graph, distance):
    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cur_cost > distance[cur_node]:
            continue

        for next_node, next_cost in graph[cur_node]:
            dist = cur_cost + next_cost

            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(queue, (dist, next_node))

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = [float('INF')] * (N + 1)
    distance[1] = 0

    dijkstra(graph, distance)

    answer = 0
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer