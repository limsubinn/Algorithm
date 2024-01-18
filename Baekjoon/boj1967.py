# 백준 1967: 트리의 지름

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(cur):
    global result
    node = cur

    queue = deque()
    queue.append(cur)

    visited = [-1] * (n+1)
    visited[cur] = 0

    while queue:
        cur = queue.popleft()

        # 기준 노드에서 가장 먼 노드 갱신
        if visited[cur] > result:
            result = visited[cur]
            node = cur

        # 연결된 노드 방문
        for next, c in graph[cur]:
            if visited[next] < 0:
                queue.append(next)
                visited[next] = visited[cur] + c

    return node

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 노드 하나를 잡고, 가장 먼 노드를 찾은 후
result = 0
cur = bfs(1)
# 그 노드에서 다시 가장 먼 노드를 찾는다.
result = 0
bfs(cur)

print(result)