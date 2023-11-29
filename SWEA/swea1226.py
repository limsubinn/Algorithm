# 1226. 미로1

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= 16 or my < 0 or my >= 16:
                continue

            # 도착
            if board[mx][my] == 3:
                return 1

            if board[mx][my] == 1:
                continue

            queue.append([mx, my])
            board[mx][my] = 1

    return 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(1, 11):
    t = int(input())

    board = []
    for i in range(16):
        temp = list(map(int, input()))
        if 2 in temp: # 시작 좌표
            x, y = i, temp.index(i)
        board.append(temp)

    print(f'#{t} {bfs(x, y)}')