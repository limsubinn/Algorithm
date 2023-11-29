# 12712. 파리퇴치3

def find(dx, dy, x, y, m, n):
    result = array[x][y] # 노즐의 중심이 향한 칸

    for i in range(1, m):
        # 이동 좌표
        tx = [i*a for a in dx]
        ty = [i*a for a in dy]

        for j in range(4):
            mx = x + tx[j]
            my = y + ty[j]

            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue

            result += array[mx][my]

    return result

T = int(input())

# 상하좌우
dx1 = [1, -1, 0, 0]
dy1 = [0, 0, 1, -1]

# 대각선
dx2 = [1, 1, -1, -1]
dy2 = [1, -1, -1, 1]

for t in range(1, T+1):
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(n):
            # 중심 좌표 잡아주기
            x, y = i, j
            # 최댓값 갱신
            answer = max(find(dx1, dy1, x, y, m, n), find(dx2, dy2, x, y, m, n), answer)

    print(f'#{t} {answer}')
