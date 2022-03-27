from collections import deque

k = int(input())
res = [[] for _ in range(k)]

def bfs(x):
    queue = deque()
    queue.append(x)

    flag = 0
    visited[x] = [1, flag]

    while queue:
        q = queue.popleft()
        flag = 1 - visited[q][1]

        for i in graph[q]:
            if visited[i][0] == 0:
                queue.append(i)
                visited[i] = [1, flag]
                for j in graph[i]:
                    if visited[i][1] == visited[j][1]:
                        return False

    return True

for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [[0, 20000] for _ in range(v + 1)]
    res[i] = "YES"
    for j in range(e):
        data = input().split()
        graph[int(data[0])].append(int(data[1]))
        graph[int(data[1])].append(int(data[0]))
    for l in range(1, v+1):
        if visited[l][0] == 0:
            if not bfs(l):
                res[i] = "NO"
                break

for i in range(k):
    print(res[i])