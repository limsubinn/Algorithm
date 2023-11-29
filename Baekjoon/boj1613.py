import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = -1 # 앞에 있는 사건이 먼저 일어난 경우
    graph[b][a] = 1 # 뒤에 있는 사건이 먼저 일어난 경우

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
            elif graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    print(graph[a][b])