# 백준 1516: 게임 개발

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def topology_sort():
    queue = deque()
    total = [0] * (n+1)

    # 진입차수가 0인 노드 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append([i, costs[i]])

    while queue:
        cur, cost = queue.popleft()
        answer[cur] = cost # 정답

        for i in graph[cur]:
            indegree[i] -= 1
            total[i] = max(total[i], cost) # 먼저 지어져야 하는 건물들을 완성하는데 걸리는 최소 시간

            if indegree[i] == 0:
                queue.append([i, total[i] + costs[i]])

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
costs = [[] for _ in range(n+1)]

for i in range(1, n+1):
    info = list(map(int, input().split()))[:-1]

    # 건물을 짓는데 걸리는 시간
    costs[i] = info[0]

    # 건물의 선후관계
    for j in range(1, len(info)):
        graph[info[j]].append(i)
        indegree[i] += 1

answer = [0] * (n+1)
topology_sort()

for i in range(1, n+1):
    print(answer[i])
