import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(i, n):
    queue = deque([i])
    visited = [False] * (n+1)
    visited[i] = True

    while queue:
        q = queue.popleft()

        for i in graph[q]:
            if visited[i]:
                continue
            queue.append(i)
            parent[i] = q
            visited[i] = True

n = int(input())

graph = [[] for i in range(n+1)] # 노드 정보 저장
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[] for i in range(n+1)]
parent[1] = 1
bfs(1, n) # 부모 찾기

for i in parent[2:]:
    print(i)