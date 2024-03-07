# 프로그래머스 12936: 줄 서는 방법

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    num = [i for i in range(1, n + 1)] # 1~n
    answer = []

    while num:
        i = (k - 1) // factorial(n - 1)

        answer.append(num[i])
        num.pop(i)

        k %= factorial(n - 1)
        n -= 1

    return answer