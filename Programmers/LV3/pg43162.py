# 프로그래머스 43162: 네트워크

from collections import deque

def bfs(node, array, visited):
    queue = deque([node])

    while queue:
        node = queue.popleft()
        visited[node] = True
        
        for i in array[node]:
            if not visited[i]:
                queue.append(i)

    return 1
            

def solution(n, computers):
    array = [[] for i in range(n)] # 연결된 노드를 저장할 배열
    for i in range(n):
        for j in range(n):
            if computers[i][j] != 0:
                array[i].append(j)

    answer = 0
    visited = [False] * n

    for i in array:
        for j in i:
            if not visited[j]:
                answer += bfs(j, array, visited)

    return answer