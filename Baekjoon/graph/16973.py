import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def isInWall(mx, my):
    for wx, wy in walls:
        if mx <= wx < mx + h and my <= wy < my + w:
            return True
    return False

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 0
    queue = deque()
    queue.append([x, y, cnt])

    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == Fr-1 and y == Fc-1:
            return cnt

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if not (0 <= mx < n) or not (0 <= my < m) or (mx + h - 1) >= n or (my + w - 1) >= m:
                continue

            if visited[mx][my]:
                continue

            if isInWall(mx, my): # 벽 좌표가 현재 직사각형 범위 안에 있는지 확인
                continue
        
            queue.append([mx, my, cnt+1])
            visited[mx][my] = True
    
    return -1

n, m = map(int, input().split())

board = []
walls = []
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(m):
        if temp[j] == 1:
            walls.append([i, j]) # 벽 좌표 저장
    
    board.append(temp)

h, w, Sr, Sc, Fr, Fc = map(int, input().split())
print(bfs(Sr-1, Sc-1))