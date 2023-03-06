# 프로그래머스 67257: 수식 최대화 (2020 카카오 인턴십)

import re
from itertools import permutations

def solution(expression):
    num = list(map(int, re.split('\+|\-|\*', expression))) # 숫자
    op = re.split('[0-9]+', expression)[1:-1] # 연산자
    per = list(permutations(set(op), len(set(op)))) # 연산자 우선순위

    answer = 0
    for p in per:
        n = num[:]
        o = op[:]

        i = 0
        while i < len(p):
            while p[i] in o:
                idx = o.index(p[i])
                tmp = o.pop(idx)

                if tmp == '+':
                    n[idx] += n.pop(idx+1)
                elif tmp == '-':
                    n[idx] -= n.pop(idx+1)
                else:
                    n[idx] *= n.pop(idx+1)
            
            i += 1
        
        answer = max(answer, abs(n[0]))
        
    return answer