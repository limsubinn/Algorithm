# 백준 1926: 그림

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    board[x][y] = 0
    width = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m or board[mx][my] == 0:
                continue

            board[mx][my] = 0
            queue.append([mx, my])
            width += 1

    return width

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mw = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if board[i][j]:
            mw = max(mw, bfs(i, j))
            cnt += 1

print(cnt)
print(mw)