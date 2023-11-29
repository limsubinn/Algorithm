import sys
import heapq

def input():
    return sys.stdin.readline().strip()

n = int(input())

# 양수, 음수 나눠서 관리
plus = []
minus = []
result = []

for _ in range(n):
    x = int(input())

    # 양수 삽입
    if x > 0:
        heapq.heappush(plus, x)
    # 음수 삽입
    elif x < 0:
        heapq.heappush(minus, -x)
    # 정답 추가
    else:
        p = m = 0
        if plus:
            p = heapq.heappop(plus)
        if minus:
            m = heapq.heappop(minus)

        if p == 0 and m == 0:
            result.append(0)
        elif p == 0:
            result.append(-m)
        elif m == 0:
            result.append(p)
        elif m > p:
            result.append(p)
            heapq.heappush(minus, m)
        else:
            result.append(-m)
            heapq.heappush(plus, p)

for i in result:
    print(i)