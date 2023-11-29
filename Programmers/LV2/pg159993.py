# 프로그래머스 159993: 미로 탈출

from collections import deque

def find_target(target, maps):
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == target:
                return [x, y]

def bfs(x, y, target, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    result = 0
    queue = deque()
    queue.append([x, y, result]) # [x, y, 이동시간]
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[x][y] = True
    
    while queue:
        x, y, result = queue.popleft()
        result += 1
        
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            
            if mx < 0 or mx >= len(maps) or my < 0 or my >= len(maps[0]):
                continue
                
            if maps[mx][my] == 'X':
                continue
            
            if visited[mx][my]:
                continue
                
            if maps[mx][my] == target:
                return [mx, my, result]
            
            queue.append([mx, my, result])
            visited[mx][my] = True
    
    return [-1]

def solution(maps):
    # 출발점 찾기
    [x, y] = find_target('S', maps)
    
    # S -> L
    result = bfs(x, y, 'L', maps)
    if result[-1] == -1:
        return -1
    answer = result[-1]
    
    # L -> E
    result = bfs(result[0], result[1], 'E', maps)
    if result[-1] == -1:
        return -1
    answer += result[-1]

    return answer