# 백준 1261: 알고스팟

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def bfs(cost, x, y):
    queue = []
    heapq.heappush(queue, [cost, x, y])

    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == n-1 and y == m-1:
            continue

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if visited[mx][my] == -1:
                visited[mx][my] = cost + miro[mx][my]
                heapq.heappush(queue, [visited[mx][my], mx, my])

    return visited[-1][-1]

m, n = map(int, input().split())
miro = [[0] * m for _ in range(n)]
for i in range(n):
    temp = list(input())
    for j in range(m):
        miro[i][j] = int(temp[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = bfs(0, 0, 0)
print(answer)
