import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

result = [[[0] * n for _ in range(n)] for _ in range(3)]
result[0][0][1] = 1

# 1행
for i in range(2, n):
    if house[0][i] == 0:
        result[0][0][i] = result[0][0][i-1]

for i in range(1, n):
    for j in range(2, n):
        # 벽이 있는 경우
        if house[i][j] != 0:
            continue

        # 대각선 -> (i-1, j-1)의 가로 + 세로 + 대각선
        if house[i][j-1] == 0 and house[i-1][j] == 0:
            result[1][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]

        # 가로 -> (i, j-1)의 가로 + 대각선
        result[0][i][j] = result[0][i][j-1] + result[1][i][j-1]

        # 세로 -> (i-1, j)의 세로 + 대각선
        result[2][i][j] = result[2][i-1][j] + result[1][i-1][j]

print(sum(result[i][n-1][n-1] for i in range(3)))