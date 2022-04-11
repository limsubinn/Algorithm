n, k = map(int, input().split())
d = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(n):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(v + d[i-1][j-w], d[i-1][j])

print(max(d[n-1]))