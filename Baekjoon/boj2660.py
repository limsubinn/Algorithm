# 백준 2660: 회장 뽑기

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(x):
    queue = deque([x])
    visited[x] = 0

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] < 0:
                queue.append(i)
                visited[i] = visited[x] + 1

    return max(visited)

n = int(input())
graph = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())

    if a == -1: # 마지막 줄
        break

    graph[a].append(b)
    graph[b].append(a)

answer = 50 # 회장 후보의 점수
candidates = [] # 회장 후보

for i in range(1, n+1):
    visited = [-1] * (n+1)
    score = bfs(i)

    # 회장 후보 및 점수 갱신
    if score < answer:
        answer = score
        candidates = [i]
    # 회장 후보 추가
    elif score == answer:
        candidates.append(i)

print(answer, len(candidates))
print(*candidates)
