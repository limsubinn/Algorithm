from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append([x, y])

    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= len(board) or my < 0 or my >= len(board[0]):
                continue

            if board[mx][my] == 1:
                board[mx][my] = 0
                visited[mx][my] = True
                continue
            
            if visited[mx][my]:
                continue

            queue.append([mx, my])
            visited[mx][my] = True

h, w = map(int, input().split())

board = [[0] * (w+2)] # 바깥 테두리 모두 0으로 채워서 입력받기
for i in range(h):
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    temp.append(0)
    board.append(temp)

time = 0 # 녹아서 없어지는 시간
result = 0 # 녹기 전 남아있는 치즈 조각
for i in board:
    result += i.count(1)

while True:
    bfs(0, 0)
    time += 1
    
    cnt = 0
    for i in board: # 녹기 전 남아있는 치즈 조각
        cnt += i.count(1)
    
    if cnt == 0: # 더이상 남아있는 치즈가 없으면 반복문 종료
        break

    result = cnt # 남아있는 치즈 갱신
    
print(time)
print(result)