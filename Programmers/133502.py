# 프로그래머스 133502: 햄버거 만들기

def solution(ingredient):
    answer = 0
    res = ''
    
    for i in ingredient:
        res += str(i)
        if res[-4:] == '1231':
            res = res[:-4]
            answer += 1

    return answer