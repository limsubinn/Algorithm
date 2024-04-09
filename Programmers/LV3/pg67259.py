# 프로그래머스 67259: 경주로 건설

import heapq

def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = []
    queue.append((0, 0, 0, 0, 0, 0))  # 비용, 방향, 현재 x y, 이전 x y

    visited = [[[float('INF')] * len(board[0]) for _ in range(len(board))] for _ in range(4)]
    for i in range(4):
        visited[i][0][0] = 0

    while queue:
        c, d, x, y, px, py = heapq.heappop(queue)

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            # 이동 불가능
            if mx < 0 or mx >= len(board) or my < 0 or my >= len(board[0]) or board[mx][my] == 1:
                continue

            # 직선 도로
            cost = c + 100
            # 곡선 도로
            if px != mx and py != my:
                cost += 500

            # 매 방향마다의 최솟값 갱신
            if cost <= visited[i][mx][my]:
                visited[i][mx][my] = cost
                heapq.heappush(queue, (cost, i, mx, my, x, y))

    # 최솟값 찾기
    answer = visited[0][-1][-1]
    for i in range(1, 4):
        answer = min(answer, visited[i][-1][-1])

    return answer