# 백준 1647: 도시 분할 계획

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return x

def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

queue = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b)) # 비용 순

cnt = 0
answer = 0
while cnt < n-2: # n-1개의 도시 연결 (간선은 n-2개)
    c, a, b = heapq.heappop(queue)
    a = find(a)
    b = find(b)
    # 도시가 연결되어 있지 않으면 연결하기
    if a != b:
        union(a, b)
        cnt += 1
        answer += c

print(answer)