# 백준 4386: 별자리 만들기

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
nodes = [list(map(float, input().split())) for _ in range(n)]

parent = [i for i in range(n)]
edges = []

for i in range(n-1):
    for j in range(i+1, n):
        # 거리
        x = nodes[i][0] - nodes[j][0]
        y = nodes[i][1] - nodes[j][1]
        cost = (x ** 2 + y ** 2) ** 0.5
        # 우선순위 큐에 삽입
        heapq.heappush(edges, (cost, i, j))

answer = 0

while edges:
    # 꺼내기
    cost, a, b = heapq.heappop(edges)
    # 사이클이 발생하지 않을 때 연결하기
    if find(a) != find(b):
        union(a, b)
        answer += cost

# 소수점 둘째 자리까지 출력
print(f'{answer:0.2f}')