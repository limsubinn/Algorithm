# 백준 12015: 가장 긴 증가하는 부분 수열 2

import sys
import bisect

def input():
    return sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))

result = [a[0]]
for i in range(1, n):
    # 리스트의 마지막 값 < a[i] -> 리스트에 삽입
    if result[-1] < a[i]:
        result.append(a[i])
    # 리스트의 마지막 값 > a[i] -> lower_bound 위치 찾아서 교체
    else:
        lower_bound = bisect.bisect_left(result, a[i])
        result[lower_bound] = a[i]

print(len(result))

'''
# 백준 12015: 가장 긴 증가하는 부분 수열 2

import sys

def input():
    return sys.stdin.readline().strip()

def binary_search(i):
    start, end = 0, len(result)-1
    while start <= end:
        mid = (start + end) // 2
        if result[mid] < a[i]:
            start = mid + 1
        else:
            end = mid - 1
    return start

n = int(input())
a = list(map(int, input().split()))

result = [a[0]]
for i in range(1, n):
    # 리스트의 마지막 값 < a[i] -> 리스트에 삽입
    if result[-1] < a[i]:
        result.append(a[i])
    # 리스트의 마지막 값 > a[i] -> lower_bound 위치 찾아서 교체
    else:
        lower_bound = binary_search(i)
        result[lower_bound] = a[i]

print(len(result))
'''