num = []
for i in range(28):
    num.append(int(input()))

answer = list(set(range(1, 31)) - set(num))
answer.sort()

for i in answer:
    print(i)