# bfs

from collections import deque

n = int(input())
m = int(input())
com = [[] for _ in range(n+1)]

for i in range(m):
    data = input().split()
    com[int(data[0])].append(int(data[1]))
    com[int(data[1])].append(int(data[0]))

def bfs(v):
    count = 0
    visited = [False] * (n+1)
    queue = deque([v])
    visited[v] = True

    while queue:
        q = queue.popleft()
        visited[q] = True
        count += 1

        for i in com[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return count-1

print(bfs(1))