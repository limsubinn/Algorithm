# dfs

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if list[y][x] == 1:
        list[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    else:
        return False

t = int(input())
count = []

for i in range(t):
    m, n, k = map(int, input().split())
    list = [[0] * m for _ in range(n)]
    count.append(0)

    for j in range(k):
        x, y = map(int, input().split())
        list[y][x] = 1

    for a in range(n):
        for b in range(m):
            if dfs(b, a):
                count[i] += 1

for i in range(t):
    print(count[i])