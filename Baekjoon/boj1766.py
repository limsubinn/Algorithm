from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

info = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    info[a].append(b)
    indegree[b] += 1

q = PriorityQueue()
res = []

for i in range(1, n+1):
    if indegree[i] == 0:
        q.put(i)

while q.empty() is False:
    now = q.get()
    res.append(now)
    for i in info[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.put(i)

for i in res:
    print(i, end=' ')
