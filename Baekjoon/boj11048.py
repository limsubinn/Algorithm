import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * (m+1) for _ in range(n+1)] # 정답 배열

for i in range(1, n+1):
    for j in range(1, m+1):
        # 위쪽 칸, 왼쪽 칸 중 최댓값 더하기
        result[i][j] = max(result[i-1][j] + board[i-1][j-1], result[i][j-1] + board[i-1][j-1])

print(result[-1][-1])