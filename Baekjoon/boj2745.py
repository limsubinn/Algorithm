import sys

def input():
    return sys.stdin.readline().strip()

n, b = input().split()
b = int(b)

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = len(n) - 1
answer = 0

for i in n:
    answer += num.index(i) * (b ** p)
    p -= 1

print(answer)