import sys

n = int(input())
card = sorted(map(int, sys.stdin.readline().split()))
m = int(input())
find = list(map(int, sys.stdin.readline().split()))

dict_card = dict()
for i in card:
    if i in dict_card:
        dict_card[i] += 1
    else:
        dict_card[i] = 1

for i in find:
    if i in dict_card:
        print(dict_card[i], end=' ')
    else:
        print(0, end=' ')