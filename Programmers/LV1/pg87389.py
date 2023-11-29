# 프로그래머스 87389: 나머지가 1이 되는 수 찾기

def solution(n):
    # n이 홀수일 때 
    if (n % 2) != 0:
        return 2

    # n이 짝수일 때
    x = n - 1
    for i in range(3, x+1):
        if x % i == 0:
            return i