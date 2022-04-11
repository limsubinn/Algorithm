n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2, -1, -1):
    for j in range(i+1):
        d[i][j] += max(d[i+1][j], d[i+1][j+1])

print(d[0][0])