# dfs

n = int(input())
m = int(input())
com = [[] for _ in range(n+1)]

for i in range(m):
    d1, d2 = map(int, input().split())
    com[d1].append(d2)
    com[d2].append(d1)

visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1

    for i in com[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1)
