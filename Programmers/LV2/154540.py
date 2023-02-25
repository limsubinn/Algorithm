# 프로그래머스 154540: 무인도 여행

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, x, y):
    queue = deque()
    queue.append([x, y])
    result = int(maps[x][y])
    maps[x][y] = 'X'
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 'X':
                continue
                
            queue.append([nx, ny])
            result += int(maps[nx][ny])
            maps[nx][ny] = 'X'
            
    return result
            
def solution(maps):
    answer = []
    maps = [list(map(str, i)) for i in maps]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                answer.append(bfs(maps, i, j))
    
    if answer == []:
        return [-1]

    answer.sort()
    return answer