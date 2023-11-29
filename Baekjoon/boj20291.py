import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

dic = {} # 확장자 별 개수
for i in range(n):
    file = input().split('.')[1]
    if file in dic:
        dic[file] += 1
    else:
        dic[file] = 1

dic = sorted(dic.items()) # 정렬

for i, j in dic:
    print(i, j)