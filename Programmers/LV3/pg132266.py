# 프로그래머스 132266: 부대 복귀

import heapq

def solution(n, roads, sources, destination):
    distance = [float('INF')] * (n + 1)
    distance[destination] = 0

    graph = [[] for _ in range(n + 1)]
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    queue = []
    heapq.heappush(queue, (destination, 0))

    # 다익스트라
    while queue:
        cur_node, cur_cost = heapq.heappop(queue)

        if distance[cur_node] < cur_cost:
            continue

        for next_node in graph[cur_node]:
            cost = cur_cost + 1
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (next_node, cost))

    answer = []
    for source in sources:
        # 복귀 가능
        if distance[source] < float('INF'):
            answer.append(distance[source])
        # 복귀 불가능
        else:
            answer.append(-1)
    return answer
