# 백준 14725: 개미굴

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

data = []
for _ in range(n):
    i = list(input().split())
    data.append(i[1:])
data.sort()

# 첫번째 줄 출력
for j in range(len(data[0])):
    print('--' * j + data[0][j])
# 두번째 줄~ 출력
for i in range(1, n):
    flag = False
    for j in range(len(data[i])):
        # 겹치는 경우
        if not flag and len(data[i-1]) > j and data[i][j] == data[i-1][j]:
            continue
        # 겹치지 않는 경우
        flag = True
        print('--' * j + data[i][j])
