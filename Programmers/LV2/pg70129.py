# 프로그래머스 70129: 이진 변환 반복하기

def solution(s):
    d = 0
    t = 0
    
    while s != '1':
        d += s.count('0')
        s = bin(s.count('1'))[2:]
        t += 1

    return [t, d]