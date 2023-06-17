import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
num = list(map(int, input().split()))

# 누적합
prefix_sum = [0] + [num[i] for i in range(n)]
for i in range(1, n+1):
    prefix_sum[i] += prefix_sum[i-1]

# 구간합
for _ in range(m):
    a, b = map(int, input().split())
    answer = prefix_sum[b] - prefix_sum[a-1]
    print(answer)
