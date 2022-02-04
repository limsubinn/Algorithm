import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    num.append([y, x])

num.sort()

for i in range(n):
    print(num[i][1], num[i][0])