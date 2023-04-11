# 프로그래머스 87694: 아이템 줍기

from collections import deque

def bfs(box, character, item):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque()
    queue.append(character) # 출발지
    
    while queue:
        x, y = queue.popleft()
        
        if [x, y] == item: # 목적지
            return box[x][y]
        
        for dx, dy in move:
            mx = x + dx
            my = y + dy
            if mx < 0 or mx >= len(box) or my < 0 or my >= len(box[0]):
                continue
            if box[mx][my] == 1:
                queue.append([mx, my])
                box[mx][my] += box[x][y]
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    box = [[-1] * 101 for _ in range(101)] # 배열 크기 2배로 잡아주기 (겹치는 선 방지)
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 이미 사각형의 내부이면 넘어간다.
                if box[i][j] == 0:
                    continue
                # 테두리 그리기
                if i == x1 or i == x2 or j == y1 or j == y2:
                    box[i][j] = 1
                    continue
                # 사각형 내부 그리기
                box[i][j] = 0
    
    # 배열의 크기가 2배이므로 정답은 2로 나누기
    # (answer에는 정답 * 2 + 1이 들어있음 -> 어차피 int형으로 반환하므로 -1을 하지 않고 진행함)
    answer = bfs(box, [characterX*2, characterY*2], [itemX*2, itemY*2]) // 2
    return answer