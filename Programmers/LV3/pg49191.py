# 프로그래머스 49191: 순위

from collections import deque

def bfs(i, n, array):
    result = 0

    queue = deque()
    visited = [False] * (n+1)
    
    for j in array[i]:
        queue.append(j)
        visited[j] = True
        result += 1

    while queue:
        i = queue.popleft()

        for j in array[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                result += 1

    return result

def solution(n, results):
    win = [[] for i in range(n+1)]
    lose = [[] for i in range(n+1)]
    for i, j in results:
        win[i].append(j)
        lose[j].append(i)

    answer = 0
    for i in range(1, n+1):
        # 이긴 경우의 수, 진 경우의 수 더하기
        result = bfs(i, n, win)
        result += bfs(i, n, lose)
        # 자신을 제외한 모든 결과가 계산되었으면 정확하게 순위를 매길 수 있다.
        if result == n-1:
            answer += 1
    return answer