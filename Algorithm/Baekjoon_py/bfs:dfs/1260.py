from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    data = input().split()
    graph[int(data[0])].append(int(data[1]))
    graph[int(data[1])].append(int(data[0]))

for i in range(n+1):
    graph[i].sort()

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

def dfs(dfs_visited, v):
    dfs_visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(dfs_visited, i)

def bfs(bfs_visited, v):
    bfs_visited[v] = True
    queue = deque([v])

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in graph[q]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

dfs(dfs_visited, v)
print()
bfs(bfs_visited, v)