# 백준 1043: 거짓말

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def bfs(x):
    queue = deque([x])
    visited = [False] * (n+1)
    visited[x] = True

    while queue:
        x = queue.popleft()

        for g in graph[x]:
            if visited[g]:
                continue
            # 진실을 아는 사람 합치기
            union(x, g)
            visited[g] = True
            queue.append(g)


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

truth = list(map(int, input().split()))
# 진실을 아는 사람이 0명일 경우
if truth[0] == 0:
    print(m)
    exit(0)
# 진실을 아는 사람 합치기
for i in range(1, len(truth)):
    union(truth[1], truth[i])

graph = [[] for _ in range(n+1)]
party = []
for _ in range(m):
    temp = list(map(int, input().split()))
    party.append(temp[1])

    if temp[0] < 2:
        continue

    # 그래프 추가
    t = temp[1]
    for i in temp[2:]:
        graph[t].append(i)
        graph[i].append(t)

# 진실을 아는 사람 탐색
for i in truth[1:]:
    bfs(i)
for i in range(1, n+1):
    parent[i] = find(i)

answer = 0
for p in party:
    # 과장된 이야기를 할 수 있는 경우
    if parent[p] != parent[truth[1]]:
        answer += 1

print(answer)