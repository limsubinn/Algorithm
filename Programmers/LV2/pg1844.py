# 프로그래머스 1844: 게임 맵 최단거리

from collections import deque

def solution(maps):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in move:
            mx = x + dx
            my = y + dy
            # 범위를 벗어난 경우
            if mx < 0 or mx >= len(maps) or my < 0 or my >= len(maps[0]):
                continue
            # 벽이 있거나, 이미 방문한 적이 있는 경우
            if maps[mx][my] != 1:
                continue
            if mx == 0 and my == 0:
                continue
            maps[mx][my] += maps[x][y]
            queue.append([mx, my])
                
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]