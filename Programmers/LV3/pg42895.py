# 프로그래머스 42895: N으로 표현

def solution(N, number):
    if N == number:
        return 1
    
    result = [[], [N]]
    i = 2

    for i in range(2, 9): # 8번까지 계산
        res = [int(str(N)*i)]
        for j in range(1, i//2+1): # 사칙연산을 수행할 케이스
            for a in result[j]:
                for b in result[i-j]:
                    res.append(a+b)
                    res.append(a-b)
                    res.append(a*b)
                    res.append(a-b)
                    if b > 0:
                        res.append(a//b)
                    if a > 0:
                        res.append(b//a)
        res = set(res)
        if number in res:
            return i
        result.append(res)

    return -1