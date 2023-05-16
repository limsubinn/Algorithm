# 1209. Sum

def row_sum(array):
    for i in array:
        result.append(sum(i))

def diagonal_sum(x, y, dx, dy):
    result.append(board[x][y])
    for _ in range(99):
        mx, my = x + dx, y + dy
        result[-1] += board[mx][my]
        x, y = mx, my

for _ in range(1, 11):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    result = []

    # 가로 합
    row_sum(board)

    # 세로 합
    board_t = list(zip(*board))
    row_sum(board_t)

    # 오른쪽 대각선 합
    diagonal_sum(0, 0, 1, 1)

    # 왼쪽 대각선 합
    diagonal_sum(99, 0, -1, 1)

    print(f'#{t} {max(result)}')


