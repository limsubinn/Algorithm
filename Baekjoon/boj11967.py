# 백준 11967: 불켜기

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(x, y, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * n for _ in range(n)]
    light = [[False] * n for _ in range(n)]

    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    light[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for a, b in rooms[x][y]:
            # 이미 불이 켜진 곳인 경우
            if light[a][b]:
                continue

            # 불 켜기
            light[a][b] = True
            cnt += 1

            for i in range(4):
                mx = a + dx[i]
                my = b + dy[i]

                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue

                # 재탐색
                if visited[mx][my]:
                    queue.append([mx, my])

        # 상하좌우 탐색
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue

            if not light[mx][my] or visited[mx][my]:
                continue

            # 불이 켜져 있고 방문한 적 없는 방인 경우
            visited[mx][my] = True
            queue.append([mx, my])

    return cnt

n, m = map(int, input().split())
rooms = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    rooms[x-1][y-1].append([a-1, b-1])

answer = bfs(0, 0, n)
print(answer)
