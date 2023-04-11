# 프로그래머스 84021: 퍼즐 조각 채우기

from collections import deque

def bfs(x, y, t, f, array, size):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    temp = []
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        array[x][y] = f
        temp.append([x, y])
        
        for dx, dy in move:
            mx = x + dx
            my = y + dy
            if mx < 0 or mx >= size or my < 0 or my >= size:
                continue
            if array[mx][my] == t:
                queue.append([mx, my])

    return temp

def make_board(array):
    x1 = min(array, key=lambda x:x[0])[0]
    x2 = max(array, key=lambda x:x[0])[0]
    y1 = min(array, key=lambda x:x[1])[1]
    y2 = max(array, key=lambda x:x[1])[1]
    sizeX = x2 - x1 + 1
    sizeY = y2 - y1 + 1
    
    temp = [[0] * sizeY for _ in range(sizeX)]
    for x, y in array:
        temp[x-x1][y-y1] = 1
        
    return temp

def rotate(array):
    r = [list(i) for i in zip(*array[::-1])]
    return r
    
    
def solution(game_board, table):
    size = len(game_board)
    board = [] # 퍼즐 조각들을 저장할 리스트
    
    for i in range(size):
        for j in range(size):
            if table[i][j] == 1:
                # table에서 이어진 퍼즐 조각을 찾고,
                temp = bfs(i, j, 1, 0, table, size)
                # 그 부분만 떼서 저장
                board.append(make_board(temp))
    
    visited = [False] * len(board) # table의 방문 여부를 체크할 리스트
    answer = 0
    check = 0 # break문을 위한 변수
    
    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 0:
                # game_board에서 이어진 빈 부분을 찾고,
                temp = bfs(i, j, 0, 1, game_board, size)
                # 그 부분만 떼서 비교
                temp = make_board(temp)
                for k in range(4):
                    # 회전
                    temp = rotate(temp)
                    # board를 순회하면서
                    for b in range(len(board)):
                        if visited[b]:
                            continue
                        # 빈 부분과 board가 같으면 방문 처리 후 정답 추가
                        if temp == board[b]:
                            visited[b] = True
                            for t in temp:
                                answer += t.count(1)
                            check = 1
                            break
                    if check == 1:
                        check = 0
                        break
                    
    return answer