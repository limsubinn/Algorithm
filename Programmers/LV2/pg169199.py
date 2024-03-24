# 프로그래머스 169199: 리코쳇 로봇

from collections import deque

def bfs(board, x, y):
    queue = deque()
    queue.append((x, y))

    # 이동 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[-1] * len(board[0]) for _ in range(len(board))]
    visited[x][y] = 0  # 출발지 방문 표시

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            # 이동하기
            cnt = 1
            while True:
                mx = x + dx[i] * cnt
                my = y + dy[i] * cnt

                # 장애물을 만나기 전 or 범위를 벗어나기 전까지 쭉 가기
                if mx < 0 or mx >= len(board) or my < 0 or my >= len(board[0]) or board[mx][my] == 'D':
                    mx -= dx[i]
                    my -= dy[i]
                    break

                cnt += 1

            # 이미 방문한 좌표인 경우
            if visited[mx][my] != -1:
                continue

            # 방문 체크
            visited[mx][my] = visited[x][y] + 1
            queue.append((mx, my))

            # 도착지를 만났을 때
            if board[mx][my] == 'G':
                return visited[mx][my]

    return -1

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                return bfs(board, i, j)