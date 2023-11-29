# 프로그래머스 81302: 거리두기 확인하기 (2021 카카오 채용연계형 인턴십)

from collections import deque

def bfs(place):
    queue = deque()
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P': # 좌표 'P'인 곳 모두 큐에 삽입
                queue.append([i, j])
    
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while queue:
        x, y = queue.pop()
        for i in range(4): # 상하좌우 탐색
            dx = x + move[i][0]
            dy = y + move[i][1]
            if 0 <= dx < 5 and 0 <= dy < 5:
                if place[dx][dy] == 'P': # 좌표가 'P'인 곳이 존재하면 거리두기 실패
                    return 0
                if place[dx][dy] == 'O': # 좌표가 'O'인 곳이 존재하면 상하좌우 한번 더 탐색
                    cnt = 0
                    for j in range(4):
                        mx = dx + move[j][0]
                        my = dy + move[j][1]
                        if 0 <= mx < 5 and 0 <= my < 5:
                            if place[mx][my] == 'P': # 좌표가 'P'인 곳의 개수 카운팅
                                cnt += 1
                        if cnt >= 2: # 좌표가 'P'인 곳이 두 곳 이상이면 거리두기 실패
                            return 0
    
    return 1
     
def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    
    return answer