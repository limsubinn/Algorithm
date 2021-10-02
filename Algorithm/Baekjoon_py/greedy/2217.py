import sys
n = int(sys.stdin.readline())
rope = []
res = []

for i in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

for i in range(n):
    res.append(rope[i] * (i + 1))

print(max(res))