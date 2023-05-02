import copy

def explode(x, y, r, c):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
  
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or mx >= r or my < 0 or my >= c:
            continue

        temp[mx][my] = 0

r, c, n = map(int, input().split())

bombs = [[0] * c for _ in range(r)]
for i in range(r):
    temp = list(input())
    for j in range(c):
        if temp[j] == 'O':
            bombs[i][j] = 2

for i in range(2, n+1):
    for x in range(r): # 값 하나씩 감소
        for y in range(c):
            if bombs[x][y] != 0:
                bombs[x][y] -= 1

    if i % 2 == 0: # 모든 칸에 폭탄 설치
        for x in range(r):
            for y in range(c):
                if bombs[x][y] == 0:
                    bombs[x][y] = 3
    else: # 3초가 지난 폭탄 폭발
        temp = copy.deepcopy(bombs)
        for x in range(r):
            for y in range(c):
                if bombs[x][y] == 0:
                    explode(x, y, r, c)
        bombs = temp[:]

for i in range(r):
    for j in range(c):
        if bombs[i][j] == 0:
            bombs[i][j] = '.'
        else:
            bombs[i][j] = 'O'
        print(bombs[i][j], end='')
    print()