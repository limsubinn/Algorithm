# 백준 14466: 소가 길을 건너간 이유 6

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited = [[False] * (n+1) for _ in range(n+1)]
    visited[x][y] = True

    cnt = 0
    while queue:
        qx, qy = queue.popleft()

        for i in range(4):
            # 길을 건너야 하는 곳이면 넘어간다.
            if i in roads[qx][qy]:
                continue

            mx = qx + dx[i]
            my = qy + dy[i]

            if mx < 1 or mx > n or my < 1 or my > n or visited[mx][my]:
                continue

            # 다른 소를 만났을 때
            if cows[mx][my]:
                cnt += 1

            visited[mx][my] = True
            queue.append([mx, my])

    return cnt


n, k, r = map(int, input().split())

roads = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, c, d = map(int, input().split())
    if c-a == -1: # 위
        roads[a][b].append(0)
        roads[c][d].append(1)
    elif c-a == 1: # 아래
        roads[a][b].append(1)
        roads[c][d].append(0)
    elif d-b == -1: # 왼쪽
        roads[a][b].append(2)
        roads[c][d].append(3)
    else: # 오른쪽
        roads[a][b].append(3)
        roads[c][d].append(2)

# 소의 위치 정보
cows = [[False] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    cows[a][b] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if cows[i][j]:
            # 만날 수 있는 소의 쌍 추가
            cnt += bfs(i, j)

answer = (k * (k-1) - cnt) // 2
print(answer)
