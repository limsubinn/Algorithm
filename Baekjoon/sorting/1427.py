n = list(input())
num = [int(i) for i in n]
num.sort(reverse=True)

for i in num:
    print(i,end='')