# 프로그래머스 42578: 위장

def solution(clothes):    
    dic = {}
    for i, j in clothes:
        if j in dic:
            dic[j].append(i)
        else:
            dic[j] = [i]
    
    answer = 1
    for i in dic: # 해당 의상을 선택하지 않는 수를 추가해서 곱한다.
        answer *= (len(dic[i]) + 1)
    
    return answer - 1 # 모두 선택하지 않는 경우의 수를 뺀다.

'''
조합을 이용한 풀이 -> TC1 시간 초과

from itertools import combinations

def solution(clothes):    
    dic = {}
    for i, j in clothes:
        if j in dic:
            dic[j].append(i)
        else:
            dic[j] = [i]
    
    answer = 0
    for i in range(len(dic)):
        c = list(combinations(dic, i+1))
        for j in c:
            temp = 1
            for k in j:
                temp *= len(dic[k])
            answer += temp
        
    return answer
'''