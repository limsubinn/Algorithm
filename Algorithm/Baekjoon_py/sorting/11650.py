import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    num.append([x, y])

num.sort()

for i in range(n):
    print(num[i][0], num[i][1])