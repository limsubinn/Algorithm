# 프로그래머스 12907: 거스름돈

def solution(n, money):
    result = [1] + [0] * n # 초기값
    for i in money:
        for j in range(i, n+1):
            result[j] += result[j-i] # (금액-동전)원 + (동전)원 = (금액)원
    return result[-1] % 1000000007

'''
선택한 동전으로 차례대로 n원을 만들 수 있는 경우의 수를 합해나가는 방식 (dp)
'''