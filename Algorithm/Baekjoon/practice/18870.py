import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_set = sorted(list(set(num)))
num_dic = {num_set[i] : i for i in range(len(num_set))}

for i in num:
    print(num_dic[i], end=' ')