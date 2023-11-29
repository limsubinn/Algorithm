import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

students = [[] for _ in range(n+1)] # 간선에 대한 정보 (순서 저장)
indegree = [0] * (n+1) # 진입차수

for _ in range(m):
    a, b = map(int, input().split())
    students[a].append(b)
    indegree[b] += 1

q = deque()
res = []

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i) # 진입차수가 0인 노드를 큐에 넣는다.

while q:
    now = q.popleft() # 큐에서 원소를 꺼내서
    res.append(now)
    for i in students[now]:
        indegree[i] -= 1 # 해당 노드에서 출발하는 간선을 제거한다.
        if indegree[i] == 0:
            q.append(i) # 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

for i in res:
    print(i, end=' ')