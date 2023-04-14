# 최적화 풀이 - 1차원 배열을 이용하여 해당 날짜에 일정의 개수를 넣는다.
# 72ms

import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

calendar = [0] * 366
for i in range(N):
    S, E = map(int, input().split())
    for j in range(S, E+1):
        calendar[j] += 1

x, y = 0, 0
answer = 0
for i in calendar:
    if i == 0:
        answer += x * y
        x, y = 0, 0
    else:
        x += 1
        y = max(y, i)
answer += x * y
print(answer)


'''
2차원 배열로 달력을 만들고, 연속된 일정을 찾아서 정답 계산
848ms

import sys

def input():
    return sys.stdin.readline().strip()

def get_plan(N):
    plan = []
    for i in range(N):
        S, E = map(int, input().split())
        plan.append([S, E])
    plan.sort(key=lambda x:(x[0], -x[1]))
    return plan

def make_calendar(plan):
    x1 = plan[0][0]
    x2 = max(plan, key=lambda x:x[1])[1]
    calendar = []
    h = 0
    for start, end in plan:
        start -= x1
        end -= x1
        for i in range(h):
            if True in calendar[i][start:end+1]:
                continue
            for j in range(start, end+1):
                calendar[i][j] = True
            break
        else:
            calendar.append([False] * (x2 - x1 + 1))
            for j in range(start, end+1):
                calendar[h][j] = True
            h += 1
    return calendar
    
N = int(input())
plan = get_plan(N)
calendar = make_calendar(plan)

x, y = 0, 0
answer = 0
for col in list(zip(*calendar)):
    if True in col:
        x += 1
        y = max(y, len(col) - col[::-1].index(True))
    else:
        answer += x * y
        x, y = 0, 0
answer += x * y
print(answer)
'''