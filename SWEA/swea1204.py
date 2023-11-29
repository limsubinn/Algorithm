# 1204. 최빈수 구하기

t = int(input())
for i in range(t):
    test_case = int(input())
    scores = list(map(int, input().split()))

    result = [0] * 101 # 각 점수의 빈도값을 저장할 리스트

    for score in scores:
        result[score] += 1

    result = list(enumerate(result))
    result.sort(key = lambda x:(-x[1], -x[0]))
    print(f'#{test_case} {result[0][0]}')