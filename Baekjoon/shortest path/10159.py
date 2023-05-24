import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
m = int(input())

graph = [[False] * n for _ in range(n)]

# 자기 자신으로 가는 간선
for i in range(n):
    graph[i][i] = True

# 비교 결과
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

for i in range(n):
    cnt = 0
    for j in range(n):
        # 서로 간선이 존재하지 않는 경우 (비교 결과를 알 수 없는 경우)
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt)