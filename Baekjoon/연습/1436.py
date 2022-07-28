n = int(input())
cnt = 0
num = 666

while cnt <= 10000:
    if '666' in str(num):
        cnt += 1

    if cnt == n:
        break

    num += 1

print(num)