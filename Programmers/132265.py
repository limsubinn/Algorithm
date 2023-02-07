# 프로그래머스 132265: 롤케이크 자르기

from collections import Counter

def solution(topping):
    answer = 0
    t1 = Counter(topping)
    t2 = set()
    
    for i in topping:
        t1[i] -= 1
        if t1[i] == 0:
            t1.pop(i)
        t2.add(i)
        
        if len(t1) == len(t2):
            answer += 1
    return answer