# 백준 9252: LCS 2

import sys

def input():
    return sys.stdin.readline().strip()

a = list(input())
b = list(input())

len_a = len(a)
len_b = len(b)

result = [[""] * (len_b+1) for _ in range(len_a+1)]

for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        if a[i-1] == b[j-1]:
            result[i][j] = result[i-1][j-1] + a[i-1]
        else:
            if len(result[i-1][j]) >= len(result[i][j-1]):
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = result[i][j-1]

answer = result[-1][-1]
print(len(answer))
print(answer)
