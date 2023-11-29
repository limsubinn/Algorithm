import sys

def input():
    return sys.stdin.readline().strip()

n, k, q, m = map(int, input().split())

# 졸고 있는 학생들
sleep = [0] * (n+3)
for i in list(map(int, input().split())):
    sleep[i] = 1

# 출석 코드를 받은 학생들
students = [0] * (n+3)
for i in list(map(int, input().split())):
    if sleep[i]: # 졸고 있으면 통과
        continue
    for j in range(i, n+3, i): # 배수의 학생들에게 출석 코드 전송
        if sleep[j]: # 졸고 있으면 통과
            continue
        students[j] = 1

# 출석 코드를 받은 학생들의 누적합
for i in range(3, n+3):
    students[i] += students[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    answer = (e - s + 1) - (students[e] - students[s-1]) # 구간 내 누적합
    print(answer)