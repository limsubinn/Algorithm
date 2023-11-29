# 프로그래머스 60058: 괄호 변환 (2020 KAKAO BLIND RECRUITMENT)

def transfer(answer, p):
    left, right = 0, 0

    if p == '': # 빈 문자열 반환
        return p
    
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        
        if left == right: # 두 균형잡힌 괄호 문자열 u, v로 분리
            u = p[:i+1]
            v = p[i+1:]

            tmp = u[:]
            while '()' in tmp:
                tmp = tmp.replace('()', '')
            
            if tmp == '': # 올바른 괄호 문자열일 때
                answer += u + transfer(answer, v)
                return answer
            
            else: # 올바른 괄호 문자열이 아닐 때
                tmp = '' # u의 첫 번째, 마지막 문자 제거 후 나머지 문자열의 괄호 방향을 뒤집어서 붙인다.
                for j in u[1:-1]:
                    if j == '(':
                        tmp += ')'
                    else:
                        tmp += '('
                answer += '(' + transfer(answer, v) + ')' + tmp
                return answer

def solution(p):
    answer = ''
    return transfer(answer, p)