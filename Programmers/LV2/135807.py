# 프로그래머스 135807: 숫자 카드 나누기

import math

def findGcd(array):
    if len(array) == 1:
        res = array[0]
    else:
        res = math.gcd(array[0], array[1])
        for i in range(2, len(array)):
            res = math.gcd(res, array[i])
    return res

def findRes(res, array):
    if res != 1:
        for i in array:
            if i % res == 0:
                res = 0 
                break
    else:
        res = 0
    return res

def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()

    a = findGcd(arrayA)
    b = findGcd(arrayB)
  
    a = findRes(a, arrayB)
    b = findRes(b, arrayA)

    return max(a, b)