n = int(input())
x_list = []
y_list = []

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(n):
    cnt = 0

    for j in range(n):
        if x_list[j] > x_list[i] and y_list[j] > y_list[i]:
            cnt += 1

    print(cnt + 1, end=' ')