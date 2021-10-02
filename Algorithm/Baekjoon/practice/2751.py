import sys

n = int(input())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

num = sorted(num)

for i in num:
    sys.stdout.write(str(i)+'\n')