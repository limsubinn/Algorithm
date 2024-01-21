# 백준 2623: 음악프로그램

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def find():
    queue = deque()

    # 진입차수가 0인 노드 넣기
    for i in range(1, n+1):
        if visited[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        answer.append(cur)

        for next in graph[cur]:
            visited[next] -= 1

            # 진입차수가 0인 노드 넣기
            if visited[next] == 0:
                queue.append(next)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(2, len(temp)):
        graph[temp[i-1]].append(temp[i])
        visited[temp[i]] += 1

answer = []
find()

if len(answer) < n:
    print(0)
else:
    for i in answer:
        print(i)