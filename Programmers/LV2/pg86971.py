# 프로그래머스 86971: 전력망을 둘로 나누기

from collections import deque

def make_graph(array, n):
    graph = [[] for i in range(n+1)]
    for i, j in array:
        graph[i].append(j)
        graph[j].append(i)
    return graph

def bfs(graph, n):
    cnt = 0
    queue = deque([1])
    visited = [False] * (n+1)
    
    while queue:
        q = queue.popleft()
        visited[q] = True
        cnt += 1
        
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)

    return cnt
        
    
def solution(n, wires):
    answer = 100
    
    for i in range(n-1):
        array = wires[:i] + wires[i+1:] # 전선 자르기
        graph = make_graph(array, n)
        cnt = bfs(graph, n)
        answer = min(answer, abs(cnt - (n - cnt)))
        
    return answer