import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
level = list(map(int, input().split())) # 난이도

result = [0] * n
for i in range(1, n):
    result[i] += result[i-1] # 누적합
    if level[i-1] > level[i]: # 실수
        result[i] += 1

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(result[y-1] - result[x-1])