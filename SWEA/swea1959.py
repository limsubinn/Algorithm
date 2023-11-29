# 1959. 두 개의 숫자열

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 더 작은 배열이 앞으로 가도록
    if n > m:
        n, m = m, n
        a, b = b, a

    result = answer = 0
    for i in range(m-n+1):
        result = 0
        # 마주보는 숫자들을 곱한 합
        for j in range(n):
            result += a[j] * b[i+j]
        # 최댓값 갱신
        answer = max(answer, result)

    print(f'#{t} {answer}')