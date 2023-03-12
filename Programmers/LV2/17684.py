# 프로그래머스 17684: 압축 (2018 KAKAO BLIND RECRUITMENT)

def solution(msg):
    dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
           'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q': 17, 'R':18,
           'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    
    if len(msg) == 1:
        return [dic[msg]]
    
    now = msg[0] # 현재 입력
    after = msg[1] # 다음 글자
    num = 27 # 사전에 추가할 번호

    answer = []
    while True:
        # 현재 입력 + 다음 글자에 해당하는 단어를 사전에 등록한다.
        answer.append(dic[now])

        if not after:
            return answer
        
        dic[now+after] = num
        msg = msg[len(now):]  
        num += 1

        # 사전에서 현재 입력과 일치하는 가장 긴 문자열을 찾는다.
        for i in range(len(msg), 0, -1):
            if msg[:i] in dic:
                now = msg[:i]
                if i >= len(msg):
                    after = ''
                else:
                    after = msg[i]
                break