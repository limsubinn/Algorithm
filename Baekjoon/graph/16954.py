from collections import deque

queue = deque()
queue.append([7, 0, True]) # 출발 좌표

board = []
walls = []
cnt = 0
for i in range(8):
    temp = list(input())
    for j in range(8):
        if temp[j] == '#':
            walls.append([i, j, False]) # 벽 좌표
            cnt += 1
    board.append(temp)

for wall in walls[::-1]:
    queue.append(wall)

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

while queue:
    # 모든 벽을 제거했을 때
    if cnt == 0:
        print(1)
        exit()
    x, y, flag = queue.popleft()
    if flag: # 캐릭터의 이동
        # 도착
        if x == 0 and y == 7:
            print(1)
            exit()
        # 현재 좌표에 벽이 있는 경우
        if board[x][y] == '#':
            continue
        # 제자리
        queue.append([x, y, True])
        # 이동
        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            # 좌표가 범위를 벗어나는 경우
            if mx < 0 or mx >= 8 or my < 0 or my >= 8:
                continue
            # 움직일 수 없는 경우
            if board[mx][my] != '.':
                continue
            queue.append([mx, my, True])
    else: # 벽의 이동
        mx, my = x+1, y
        # 현재 좌표 벽 제거
        board[x][y] = '.'
        # 이동할 좌표가 범위를 벗어나는 경우
        if mx >= 8:
            cnt -= 1
            continue
        # 벽 이동
        board[mx][my] = '#'
        queue.append([mx, my, False])
    
print(0)