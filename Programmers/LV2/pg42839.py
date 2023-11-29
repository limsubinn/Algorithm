# 프로그래머스 42839: 소수 찾기

from itertools import permutations

def find_prime(n): # 소수 판별
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num = []
    
    for i in range(len(numbers)):
        # 숫자 조합
        c = set(permutations(list(numbers), i+1))
        for j in c:
            n = int("".join(j))
            # 중복 제거
            if n in num:
                continue
            num.append(n)
            # 소수 찾기
            if (find_prime(n)):
                answer += 1
            
    return answer