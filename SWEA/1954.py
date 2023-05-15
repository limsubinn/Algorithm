# 1954. 달팽이 숫자

from collections import deque

def sol():
    queue = deque()
    queue.append([0, 0, 0, 1])

    while queue:
        x, y, m, cnt = queue.popleft()

        # 숫자 채우기
        result[x][y] = cnt

        # 모든 숫자를 채웠을 경우 종료
        if cnt >= n**2:
            break

        # 다음 칸 이동
        mx = x + move[m][0]
        my = y + move[m][1]
        cnt += 1

        # 방향 바꾸기
        if (mx < 0 or mx >= n or my < 0 or my >= n) or result[mx][my]:
            m += 1
            if m >= 4:
                m = 0
            mx = x + move[m][0]
            my = y + move[m][1]

        queue.append([mx, my, m, cnt])
        

t = int(input())
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for test_case in range(1, t+1):
    n = int(input())

    result = [[[] for _ in range(n)] for _ in range(n)]
    sol()

    print(f'#{test_case}')
    for i in range(n):
        for j in range(n):
            print(result[i][j], end=' ')
        print()