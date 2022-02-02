from collections import deque

m, n = map(int, input().split())
tomato = []

for i in range(n):
    tomato.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if tomato[mx][my] == 0:
                queue.append([mx, my])
                tomato[mx][my] = tomato[x][y] + 1

bfs()
res = max(map(max, tomato)) - 1
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            res = -1
            break

print(res)