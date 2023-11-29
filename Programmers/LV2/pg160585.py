# 프로그래머스 160585: 혼자서 하는 틱택토

from collections import deque

def find_bingo(x, y, move, board):
    result = 1
    queue = deque()
    queue.append([x, y, result])
    
    visited = [[False] * 3 for _ in range(3)]
    visited[x][y] = True
    
    target = board[x][y]
    
    while queue:
        x, y, result = queue.popleft()
        
        for dx, dy in move:
            mx = x + dx
            my = y + dy
            
            if mx < 0 or mx >= 3 or my < 0 or my >= 3:
                continue
            
            if visited[mx][my]:
                continue
                
            if board[mx][my] != target:
                return False     
                
            queue.append([mx, my, result + 1])
            visited[mx][my] = True
    
    if result < 3:
        return False
    
    return True

def answer(board, target):
    direction = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]],
                 [[1, -1], [-1, 1]], [[1, 1], [-1, -1]]]
    ox = {'O': False, 'X': False}
    
    for x in range(3):
        for y in range(3):
            if board[x][y] == '.':
                continue
            for i in range(4):
                if find_bingo(x, y, direction[i], board):
                    ox[board[x][y]] = find_bingo(x, y, direction[i], board)
                if ox[target]:
                    return 0
    
    return 1
                    
def solution(board): 
    cnt = [0, 0] # O, X 개수
    for i in board:
        cnt[0] += i.count('O')
        cnt[1] += i.count('X')
    
    # X가 이기거나 아무도 이기지 않는 경우 1
    if (cnt[0] == cnt[1]):
        return answer(board, 'O')
    # O가 이기거나 아무도 이기지 않는 경우 1
    elif (cnt[0] == cnt[1] + 1):
        return answer(board, 'X')
    else:
        return 0