N = int(input())
problem = list(input())

check = ['R', 'B']
answer = [1, 1]

for i in range(2):
    temp = False
    for p in problem:
        if p != check[i]:
            if not temp:
                answer[i] += 1
                temp = True
        else:
            temp = False

print(min(answer))