n, m = map(int, input().split())
list = [[] for _ in range(n)]

for i in range(n):
    data = input()
    for j in range(m):
        list[i].append(int(data[j]))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # x, y 좌표가 맵을 벗어나면
        return False
    if list[x][y] == 0: # 얼음 틀에 구멍이 뚫려 있는 부분
        list[x][y] = 1 # 방문 체크
        # 상, 하, 좌, 우 체크
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    else:
        return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)