# 백준 2812: 크게 만들기

import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
number = input()

stack = []
for num in number:
    # 현재 숫자보다 작은 숫자들 제거
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    # 현재 숫자 삽입
    stack.append(num)

# 남은 숫자 제거
while k > 0:
    stack.pop()
    k -= 1

print(''.join(stack))