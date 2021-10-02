from collections import Counter
import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

print(round(sum(num)/n))

num.sort()
print(num[n//2])

counter = Counter(num).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])

print(max(num)-min(num))