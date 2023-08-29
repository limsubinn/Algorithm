import sys

def input():
    return sys.stdin.readline().strip()

def change_board(x, y, size, value):
    for i in range(x, x+size):
        for j in range(y, y+size):
            board[i][j] = value

def dfs(x, y, cnt):
    global answer

    # x가 범위를 벗어나면 탐색 완료
    if x >= 10:
        answer = min(answer, cnt)
        return

    # y가 범위를 벗어나면 다음 행 탐색
    if y >= 10:
        dfs(x+1, 0, cnt)
        return

    # 색종이를 붙일 수 없는 경우 다음 칸 탐색
    if board[x][y] == 0:
        dfs(x, y+1, cnt)
        return

    # 크기 1 ~ 5 색종이 붙이기
    for k in range(5):
        # 해당 사이즈의 색종이를 5개 이상 사용한 경우 넘어간다.
        if paper[k] >= 5:
            continue

        # 범위를 벗어난 경우 넘어간다.
        if x+k >= 10 or y+k >= 10:
            continue

        # 색종이를 붙일 크기 재기
        flag = True
        for i in range(x, x+k+1):
            for j in range(y, y+k+1):
                # 색종이를 붙일 수 없는 경우 반복문 종료
                if board[i][j] == 0:
                    flag = False
                    break
            if not flag:
                break

        # 색종이를 붙일 수 없는 경우
        if not flag:
            continue

        change_board(x, y, k+1, 0) # 색종이 붙이기
        paper[k] += 1 # 해당 사이즈의 색종이 개수 추가

        # 개수 늘린 후 다음 종이 탐색
        dfs(x, y+k+1, cnt+1)

        change_board(x, y, k+1, 1) # 색종이 떼기
        paper[k] -= 1 # 해당 사이즈의 색종이 개수 감소

board = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 5 # 색종이 개수

answer = 26
dfs(0, 0, 0)

if answer == 26:
    answer = -1

print(answer)
