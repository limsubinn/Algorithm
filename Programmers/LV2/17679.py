# 프로그래머스 17679: 프렌즈 4블록 (2018 KAKAO BLIND RECRUITMNET)

from collections import deque

def search(x, y, m, n, board):
    s = board[x][y]
    if not s:
        return
    
    move = [[0, 1], [1, 0], [1, 1]] # 오른쪽, 아래, 대각선
    result = [(x, y)]

    for mx, my in move:
        dx = x + mx
        dy = y + my

        # 주어진 범위를 벗어났을 경우 블록을 지울 수 없다.
        if dx < 0 or dx >= m or dy < 0 or dy >= n:
            result = []
            break

        # 다른 모양의 블록일 경우 블록을 지울 수 없다.
        if board[dx][dy] != s:
            result = []
            break
        
        # 같은 모양의 블록 좌표 저장
        result.append((dx, dy))
    
    if result:
        return result
    else:
        return

def solution(m, n, board):
    board = [list(i) for i in board]
    answer = 0

    while True:
        result = []
        for x in range(m):
            for y in range(n):
                res = search(x, y, m, n, board) # 4블록 찾기
                if res:
                    for r in res:
                        if r not in result: # 중복 제거
                            result.append(r)

        # 더이상 지울 블록이 없다면 정답 리턴
        if len(result) == 0: 
            break
        # 제거한 블록의 개수 추가
        answer += len(result)

        # 제거할 블록을 모두 먼저 지운다.
        for x, y in result[::-1]:
            board[x][y] = ''

        # 블록을 내려 빈 블록을 채운다.
        for x, y in result[::-1]:
            if board[x][y] == '':
                tmp = deque()
                tmp.append([x, y]) # 빈 블록을 저장할 큐
                tx = x
                while True:
                    tx -= 1 # 위쪽의 블록 탐색
                    # 인덱스의 범위를 벗어날 경우 전부 빈 블록
                    if tx < 0:
                        while tmp:
                            i, j = tmp.popleft()
                            board[i][j] = ''
                        break
                    # 위쪽에 블록이 존재할 경우 블록을 채운다.
                    if board[tx][y]:
                        i, j = tmp.popleft()
                        board[i][j] = board[tx][y]
                    tmp.append([tx, y])
    
    return answer