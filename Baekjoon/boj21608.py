import sys

def input():
    return sys.stdin.readline().strip()

def find_seat(seats, classroom, student, x, y, n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    blank = 0
    preference = 0

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or mx >= n or my < 0 or my >= n:
            continue

        if not classroom[mx][my]:
            blank += 1
            continue
        
        if classroom[mx][my] in student:
            preference += 1
    
    seats.append([preference, blank, x, y])
    
    if preference == 0: return 0
    return 10 ** (preference - 1)
    
n = int(input())
classroom = [[0] * n for _ in range(n)]
students = [[] for _ in range(n*n+1)]

for i in range(n*n):
    s = list(map(int, input().split()))
    students[s[0]] = s[1:]

    seats = []
    for x in range(n):
        for y in range(n):
            if not classroom[x][y]:
                find_seat(seats, classroom, students[s[0]], x, y, n)
    seats.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))

    x, y = seats[0][2], seats[0][3]
    classroom[x][y] = s[0]

answer = 0
for x in range(n):
    for y in range(n):
        answer += find_seat(seats, classroom, students[classroom[x][y]], x, y, n)

print(answer)