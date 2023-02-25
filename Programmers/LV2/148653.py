# 프로그래머스 14853: 마법의 엘리베이터

def solution(storey):
    answer = 0
    c = len(str(storey)) - 1
    temp = storey // 10**c
    
    while True:
        if temp < 5:
            answer += temp
            storey %= 10**c
        elif temp == 5:
            if c == 0:
                answer += 5
                break
            if (int(str(storey)[-c])) >= 5:
                answer += 1
                storey = 10**(c+1) - storey
            else:
                answer += temp
                storey %= 10**c
        else:
            answer += 1
            storey = 10**(c+1) - storey
        
        if (temp == storey) and c == 0:
            break

        c = len(str(storey)) - 1
        temp = storey // 10**c
        
    return answer