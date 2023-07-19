def get_cnt():
    max_cnt = 0

    for i in range(n):
        # 행 순회하면서 가장 긴 연속 부분 수열 찾기
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        # 열 순회하면서 가장 긴 연속 부분 수열 찾기
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt


n = int(input())
board = [list(input()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(1, n):
        # 왼쪽 비교
        if board[i][j-1] != board[i][j]:
            # 교환
            board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
            # 최댓값 갱신
            answer = max(answer, get_cnt())
            # 되돌리기
            board[i][j-1], board[i][j] = board[i][j], board[i][j-1]

        # 위쪽 비교
        if board[j-1][i] != board[j][i]:
            # 교환
            board[j-1][i], board[j][i] = board[j][i], board[j-1][i]
            # 최댓값 갱신
            answer = max(answer, get_cnt())
            # 되돌리기
            board[j-1][i], board[j][i] = board[j][i], board[j-1][i]

print(answer)
