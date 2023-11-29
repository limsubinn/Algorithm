from collections import deque

m, n, h = map(int, input().split())
tomato = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        data = list(map(int, input().split()))
        tomato[i].append(data)

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])

def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            mx = x + dx[i]
            my = y + dy[i]
            mz = z + dz[i]

            if mx < 0 or mx >= n or my < 0 or my >= m or mz < 0 or mz >= h:
                continue

            if tomato[mz][mx][my] == 0:
                queue.append([mz, mx, my])
                tomato[mz][mx][my] = tomato[z][x][y] + 1

bfs()
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            res = max(res, max(tomato[i][j]))
print(res-1)