import sys
import copy
from collections import deque

def input():
    return sys.stdin.readline().strip()

def make_board():
    idx = [[] for _ in range(26)]

    for i in range(5):
        board = list(map(int, input().split()))
        for j in range(5):
            idx[board[j]] = [i, j]
    
    return idx

def find_bingo(x, y, direction, visited):
    move = [[[1, 0], [-1, 0]], # 세로
            [[0, 1], [0, -1]], # 가로
            [[-1, -1], [1, 1]], # 오른쪽으로 내려가는 대각선
            [[1, -1], [-1, 1]]] # 왼쪽으로 내려가는 대각선
    result = 0
    v = copy.deepcopy(visited)
    queue = deque()
    queue.append([x, y, v])

    while queue:
        x, y, visit = queue.popleft()

        temp = copy.deepcopy(visit)
        temp[x][y] = True

        result += 1

        if result == 5:
            return 1
        
        for dx, dy in move[direction]:
            mx = x + dx
            my = y + dy

            if mx < 0 or mx >= 5 or my < 0 or my >= 5:
                continue

            if temp[mx][my]:
                continue

            queue.append([mx, my, temp])
    
    return 0

def game(idx):
    cnt = 0
    result = 0
    answer = 0
    visited = [[True] * 5 for _ in range(5)]

    for i in range(5):
        num = list(map(int, input().split()))

        for n in num:
            if answer > 0:
                break

            x, y = idx[n]
            visited[x][y] = False
            result += 1

            for direction in range(4):
                cnt += find_bingo(x, y, direction, visited)

                if cnt >= 3:
                    answer = result
                    break
    
    return answer

idx = make_board()
answer = game(idx)
print(answer)