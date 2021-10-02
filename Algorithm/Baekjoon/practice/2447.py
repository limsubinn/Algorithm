def star(s):
    list = []
    num = len(s)

    for i in range(3 * num):
        if i // 3 == 1:
            list.append(s[i % num] + ' ' * num + s[i % num])
        else:
            list.append(s[i % num] * 3)

    return list


n = int(input())
s = ['***', '* *', '***']
k = 0

while n != 3:
    n //= 3
    k += 1

for i in range(k):
    s = star(s)

for i in s:
    print(i)