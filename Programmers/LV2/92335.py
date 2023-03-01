# 프로그래머스 92335: k진수에서 소수 개수 구하기 (2022 KAKAO BLIND RECRUITMENT)

def findPrime(num): # 소수 찾기
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    s = ''
    while n > 0: # k진수로 변환
        s = str(n % k) + s
        n //= k
    
    answer = 0
    for i in s.split('0'):
        if i != '':
            if (findPrime(int(i))):
                answer += 1
            
    return answer