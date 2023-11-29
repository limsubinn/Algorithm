n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

for i in range(n):
    for j in range(n):
        # 도착
        if i == n-1 and j == n-1:
            break
        move = board[i][j]
        # 아래 이동이 가능할 때
        if i + move < n:
            visited[i + move][j] += visited[i][j]
        # 오른쪽 이동이 가능할 때
        if j + move < n:
            visited[i][j + move] += visited[i][j]

print(visited[-1][-1])
