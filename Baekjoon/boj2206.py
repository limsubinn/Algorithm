from collections import deque

n, m = map(int, input().split())
list = [[] for _ in range(n)]

for i in range(n):
    data = input()
    for j in range(m):
        list[i].append(int(data[j]))

def bfs(x, y, z):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([x, y, z])

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[x][y][z] = 1

    while queue:
        qx, qy, qz = queue.popleft()

        if qx == n-1 and qy == m-1:
            return visited[qx][qy][qz]

        for i in range(4):
            mx = qx + dx[i]
            my = qy + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if list[mx][my] == 1 and qz == 1:
                visited[mx][my][0] = visited[qx][qy][1] + 1
                queue.append([mx, my, 0])
            elif list[mx][my] == 0 and visited[mx][my][qz] == 0:
                visited[mx][my][qz] = visited[qx][qy][qz] + 1
                queue.append([mx, my, qz])

    return -1

print(bfs(0, 0, 1))