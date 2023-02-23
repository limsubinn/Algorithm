# 프로그래머스 12914: 멀리 뛰기

def solution(n):
    res = [0] * 2001
    res[1] = 1
    res[2] = 2
    
    for i in range(3, n+1):
        res[i] = res[i-1] + res[i-2]
        
    return res[n] % 1234567

'''
재귀 -> 시간 초과

import sys
sys.setrecursionlimit(10000)

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (solution(n-1) + solution(n-2)) % 1234567
'''

'''
다른 풀이

def solution(n):
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
 
    return b % 1234567
'''