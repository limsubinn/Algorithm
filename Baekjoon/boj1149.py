n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    d[i][0] += min(d[i-1][1], d[i-1][2])
    d[i][1] += min(d[i-1][0], d[i-1][2])
    d[i][2] += min(d[i-1][0], d[i-1][1])

print(min(d[n-1]))