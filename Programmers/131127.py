# 프로그래머스 131127: 할인 행사

from collections import Counter

def solution(want, number, discount): 
    wan = {}
    for i in range(len(want)):
        wan[want[i]] = number[i]

    answer = 0    
    dis = Counter(discount[:10])
    
    for i in range(len(discount) - 9):
        res = 0
        for j in wan:
            if wan[j] <= dis[j]:
                res += 1
        if (res == len(want)):
            answer += 1
        dis[discount[i]] -= 1

        if i == len(discount) - 10:
            return answer

        if discount[10+i] in dis:
            dis[discount[10+i]] += 1
        else:
            dis[discount[10+i]] = 1