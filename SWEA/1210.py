# 1210. Ladder1

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    visited = [[False] * 100 for _ in range(100)]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        # 출발 지점을 만나면 종료
        if x == 0:
            return y

        for i in range(3):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= 100 or my < 0 or my >= 100:
                continue

            if visited[mx][my]:
                continue

            # 이동 가능한 통로를 만났을 때
            if board[mx][my] == 1:
                visited[mx][my] = True
                queue.append([mx, my])
                break

# 좌우 먼저 살피고 위로 이동
dx = [0, 0, -1]
dy = [1, -1, 0]

for _ in range(1, 11):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점 찾기
    y = board[-1].index(2)
    # 도착 지점부터 거슬러 올라간다.
    print(f'#{t} {bfs(99, y)}')