# 2819. 격자판의 숫자 이어붙이기

def dfs(x, y, result, cnt):
    result += board[x][y]

    if cnt >= 6: # 6번 이동했으면 종료
        answer.add(result)
        return

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or mx >= 4 or my < 0 or my >= 4:
            continue

        dfs(mx, my, result, cnt+1)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for t in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    answer = set() # 중복 제거

    for x in range(4):
        for y in range(4):
            dfs(x, y, '', 0)

    print(f'#{t} {len(answer)}')