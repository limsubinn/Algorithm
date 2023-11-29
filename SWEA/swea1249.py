# 1249. 보급로

from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0])

    result = [[float('INF')] * n for _ in range(n)]
    result[0][0] = board[0][0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue

            # 최솟값 갱신
            if result[x][y] + board[mx][my] < result[mx][my]:
                result[mx][my] = result[x][y] + board[mx][my]
                queue.append([mx, my])

    return result[-1][-1]

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    print(f'#{t} {bfs()}')