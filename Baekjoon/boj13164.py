import sys

def input():
    return sys.stdin.readline().strip()

N, K = map(int, input().split())
heights = list(map(int, input().split()))

diff = []
for i in range(1, len(heights)):
    diff.append(heights[i] - heights[i-1])
diff.sort()

answer = sum(diff[:N-K])
print(answer)

'''
기존 풀이 -> 조합을 이용하여 완전 탐색으로 풀었음 (메모리 초과)
'''