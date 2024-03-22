# 프로그래머스 12905: 가장 큰 정사각형 찾기

def solution(board):
    result = [[0] * len(board[0]) for _ in range(len(board))]
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            # 정사각형을 만들 수 없는 경우
            if board[i][j] == 0:
                continue
            # 만들 수 있는 정사각형의 최대 넓이 구하기
            if i == 0 or j == 0:
                result[i][j] = 1
            else:
                result[i][j] = (min(result[i - 1][j - 1], result[i - 1][j], result[i][j - 1]) ** 0.5 + 1) ** 2
            answer = max(answer, result[i][j])

    return answer