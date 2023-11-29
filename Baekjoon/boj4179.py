from collections import deque

r, c = map(int, input().split())

queue = deque()
board = []
for i in range(r):
    temp = list(input())
    for j in range(c):
        if temp[j] == 'J':
            pos = [i, j]
            continue
        if temp[j] == 'F': # 불이 있는 곳 먼저 큐에 모두 삽입
            queue.append([i, j, -1])
    board.append(temp)
queue.append([pos[0], pos[1], 0]) # 지훈이의 초기 위치 큐에 삽입

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y, time = queue.popleft()

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if time < 0: # 불 이동
            # 범위를 벗어나면 넘어간다.
            if mx < 0 or mx >= r or my < 0 or my >= c:
                continue
            # 벽이거나 이미 불이 존재하는 곳이면 넘어간다.
            if board[mx][my] == '#' or board[mx][my] == 'F':
                continue
            board[mx][my] = 'F'
            queue.append([mx, my, -1])
        else: # 지훈 이동
            # 범위를 벗어나면(탈출 성공) 정답 출력
            if mx < 0 or mx >= r or my < 0 or my >= c:
                print(time + 1)
                exit()
            # 지훈이가 이동할 수 없는 곳이면 넘어간다.
            if board[mx][my] != '.':
                continue
            board[mx][my] = 'J'
            queue.append([mx, my, time + 1])

print("IMPOSSIBLE")