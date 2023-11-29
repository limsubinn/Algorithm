# 프로그래머스 17687: n진수 게임 (2018 KAKAO BLIND RECRUITMENT)

def change_num(num, n):
    result = ''
    dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    if num == 0:
        return '0'
    
    while num > 0: # n진수 변환
        tmp = num % n
        if tmp >= 10:
            tmp = dic[tmp]
        else:
            tmp = str(tmp)
        result = tmp + result
        num //= n

    return result

def solution(n, t, m, p):
    answer = ''
    i, j, k = 0, 0, 0

    while k < t:
        idx = k * m + p - 1 # 말해야 하는 순서
        num = change_num(i, n)

        for s in num:
            if j == idx: # 말해야 하는 순서가 되면 정답에 추가
                answer += s
                k += 1
            j += 1
        i += 1 # 숫자 증가

    return answer