# dfs

n = int(input())
list = [[] for _ in range(n)]

for i in range(n):
    data = input()
    for j in range(n):
        list[i].append(int(data[j]))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if list[x][y] == 1:
        global count
        count += 1
        list[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    else:
        return False

cList = []
result = 0

for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            cList.append(count)
            result += 1

cList.sort()
print(result)
for i in range(len(cList)):
    print(cList[i])