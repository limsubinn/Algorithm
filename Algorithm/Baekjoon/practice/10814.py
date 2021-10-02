import sys
n = int(sys.stdin.readline())
mem = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    mem.append([int(age), name])

mem.sort(key = lambda m : m[0])

for i in mem:
    print(i[0], i[1])