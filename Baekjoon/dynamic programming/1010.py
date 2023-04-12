def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    answer = factorial(M) // (factorial(N) * factorial(M-N))
    print(answer)