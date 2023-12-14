# 백준 2138: 전구와 스위치

import sys
import copy

def input():
    return sys.stdin.readline().strip()

def change(array):
    cnt = 0
    for i in range(1, len(array)):
        # 앞의 전구 상태가 다른 경우
        if array[i - 1] != after[i - 1]:
            # 상태 바꾸기
            array[i - 1] = 1 - array[i - 1]
            array[i] = 1 - array[i]
            if i + 1 < len(before):
                array[i + 1] = 1 - array[i + 1]
            # 개수 증가
            cnt += 1
    return cnt

n = int(input())
before = list(map(int, input()))
after = list(map(int, input()))

answer = 0

# 첫 번째 스위치를 누르지 않는 경우
temp = copy.deepcopy(before)
answer = change(temp)

if temp == after:
    print(answer)
    exit(0)

# 첫 번째 스위치를 누르는 경우
before[0] = 1 - before[0]
before[1] = 1 - before[1]
answer = change(before) + 1

if before == after:
    print(answer)
else:
    print(-1)