def hanoi(n, a, b, c, list):
    if n == 1:
        list.append(f'{a} {b}')
    else:
        hanoi(n-1, a, c, b, list)
        list.append(f'{a} {b}')
        hanoi(n-1, c, b, a, list)

n = int(input())
list = []
hanoi(n, 1, 3, 2, list)

print(len(list))

for i in list:
    print(i)