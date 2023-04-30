import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(i):
    cnt = 0
    queue = deque([i])

    visited = [False] * (len(relations) + 1)
    visited[i] = True

    while queue:
        i = queue.popleft()
        cnt += 1

        for r in relations[i]:
            if visited[r]:
                continue
            queue.append(r)
            visited[r] = True

    return cnt

n, m = map(int, input().split())

relations = [[] for i in range(n+1)] # 신뢰 관계 저장
for i in range(m):
    a, b = map(int, input().split())
    relations[b].append(a)

answer = []
res = 0 # 최댓값을 판별할 변수
for i in range(1, n+1):
    if not relations[i]:
        continue

    cnt = bfs(i)
    if cnt > res:
        answer = [i]
        res = cnt
        continue
    if cnt == res:
        answer.append(i)

for i in answer:
    print(i, end=' ')