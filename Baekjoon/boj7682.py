# 백준 7682: 틱택토

import sys

def input():
    return sys.stdin.readline().strip()

def get_count():
    cx, co = 0, 0
    for i in range(3):
        cx += board[i].count('X')
        co += board[i].count('O')
    return [cx, co]

def get_turn(cx, co):
    if cx == co:
        turn = 'O'
    elif cx == co + 1:
        turn = 'X'
    else:
        turn = False

    return turn

def is_success(x, y):
    cur = board[x][y]

    if cur == '.':
        return False

    for i in range(4):
        s = 1

        for j in range(1, 3):
            mx = x + dx[i] * j
            my = y + dy[i] * j

            if 0 <= mx < 3 and 0 <= my < 3 and board[mx][my] == cur:
                s += 1

        if s >= 3:
            return True

    return False

# 오른쪽, 아래쪽, 대각선 오른쪽 아래, 대각선 왼쪽 아래
dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

while True:
    temp = input()

    # 입력의 마지막
    if temp == 'end':
        break

    # 게임판
    board = [[] for _ in range(3)]
    for i in range(3):
        board[i] = list(temp[i*3:(i+1)*3])

    # 현재 순서
    cx, co = get_count()
    turn = get_turn(cx, co)
    if not turn:
        print("invalid")
        continue

    # 한 줄을 잇는지 확인
    success = 0
    flag = True
    for i in range(3):
        for j in range(3):
            s = is_success(i, j)
            if s:
                if board[i][j] != turn:
                    flag = False
                    break
                success += 1
        if not flag:
            break

    # 현재 순서와 성공한 사람이 맞지 않을 경우
    if not flag:
        print("invalid")
        continue

    # 성공한 사람이 없고, 게임판이 가득 차지 않은 경우
    if success == 0 and cx + co < 9:
        print("invalid")
        continue

    print("valid")
