import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().strip()

n, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(n)]
dishes += dishes[:k-1] # 회전

result = defaultdict(int)
result[c] = 1

# 초기값
cnt = 1
for i in range(k):
    if result[dishes[i]] == 0:
        cnt += 1
    result[dishes[i]] += 1
answer = cnt

for i in range(k, len(dishes)):
    # 초밥 빼기
    result[dishes[i-k]] -= 1
    if result[dishes[i-k]] == 0:
        cnt -= 1

    # 초밥 더하기
    if result[dishes[i]] == 0:
        cnt += 1
    result[dishes[i]] += 1

    # 정답 갱신
    answer = max(answer, cnt)

print(answer)