def make_board(board, N, number):
    move = [[-1, 0], [0, 1], [1 ,0], [0, -1]] # 상->우->하->좌 순서대로 움직임
    x, y = N//2, N//2 # 시작 좌표
    answer = [x+1, y+1] # number가 속해있는 좌표
    m, cnt = 0, 1 # 움직일 방향을 결정, 움직이는 횟수를 결정

    while True:
        # 2번씩 같은 cnt로 움직인다.
        for i in range(2):
            for j in range(cnt):
                mx = x + move[m][0]
                my = y + move[m][1]

                if mx < 0:
                    return answer

                board[mx][my] += board[x][y]

                if board[mx][my] == number:
                    answer = [mx+1, my+1]

                x, y = mx, my
            # cnt만큼 움직였으면 방향을 바꾼다.
            m += 1
            if m > 3:
                m = 0
        cnt += 1

N = int(input())
number = int(input())

board = [[1] * N for _ in range(N)]
answer = make_board(board, N, number)

for i in board:
    for j in i:
        print(j, end=' ')
    print()
print(answer[0], answer[1])