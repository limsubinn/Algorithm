# 프로그래머스 43164: 여행경로

from collections import deque

def bfs(i, tickets):
    result = ['ICN'] # 이동 경로 저장
    visited = [False] * len(tickets) # 방문 노드 저장

    queue = deque()
    queue.append([i, visited, result])

    while queue:
        i, visited, result = queue.popleft()

        res = result[:]
        res.append(tickets[i][1])

        v = visited[:]
        v[i] = True

        for j in range(len(tickets)):
            if v[j]:
                continue
            if tickets[j][0] == tickets[i][1]:
                queue.append([j, v, res])

        if len(res) == len(tickets) + 1: # 모든 티켓을 사용하면 리턴
            return res
        
    return []


def solution(tickets):
    tickets.sort(key=lambda x:x[1]) # 도착지를 기준으로 정렬

    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN': # 맨 처음 출발지
            answer = bfs(i, tickets)
            if answer:
                return answer