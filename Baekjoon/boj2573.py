import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs():
    queue = deque()
    queue.append(ice[0])

    visited = [[False] * m for _ in range(n)]
    visited[ice[0][0]][ice[0][1]] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt = 0
    melted = [] # 녹일 빙산 리스트

    while queue:
        x, y = queue.popleft()

        cnt += 1 # 탐색한 빙산의 개수
        sea = 0 # 인접한 바다의 개수

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            # 인접한 곳에 바다가 있는 경우
            if board[mx][my] == 0:
                sea += 1
                continue

            if visited[mx][my]:
                continue

            queue.append([mx, my])
            visited[mx][my] = True

        if sea > 0:
            melted.append([x, y, sea])

    for x, y, sea in melted:
        # 빙산 녹이기
        if board[x][y] - sea > 0:
            board[x][y] -= sea
        else:
            board[x][y] = 0
        
        # 제거된 빙산
        if board[x][y] == 0 and [x, y] in ice:
            ice.remove([x, y])

    return cnt

n, m = map(int, input().split())

board = []
ice = [] # 빙산이 있는 곳의 좌표 저장
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] > 0:
            ice.append([i, j])
    board.append(temp)

answer = 0
while True:
    # 빙산이 두 덩어리 이상으로 분리된 경우
    # (한 번의 실행으로 빙산을 모두 제거하지 못한 경우)
    if len(ice) != bfs():
        break

    answer += 1

    # 빙산이 다 녹을 때까지 분리되지 않은 경우
    if sum(map(sum, board[1:-1])) == 0:
        answer = 0
        break

print(answer)