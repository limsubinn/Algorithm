# 1979. 어디에 단어가 들어갈 수 있을까

from collections import deque

def find(array):
    answer = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                if solution(i, j, array):
                    answer += 1
    return answer

def solution(x, y, array):
    queue = deque()
    queue.append([x, y, 1])
    array[x][y] = 0

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(2):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue

            if array[mx][my] == 0:
                continue

            queue.append([mx, my, cnt+1])
            array[mx][my] = 0 # 방문 표시
    
    if cnt == k:
        return True
    return False

T = int(input())

# 가로만 체크
dx = [0, 0]
dy = [1, -1]

for t in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    board2 = [list(i) for i in zip(*board)] # 전치행렬

    answer = find(board)
    answer += find(board2)
    print(f'#{t} {answer}')