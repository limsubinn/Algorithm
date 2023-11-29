# 1926. 간단한 369 게임

n = int(input())

for i in range(1, n+1):
    num = list(str(i))

    cnt = 0
    for j in num: # 3, 6, 9가 나오는 횟수
        if j == '3' or j == '6' or j == '9':
            cnt += 1

    if cnt > 0: # 박수 출력
        print('-' * cnt, end = ' ')
    else: # 숫자 출력
        print(i, end = ' ')