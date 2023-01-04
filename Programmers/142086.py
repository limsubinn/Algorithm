# 프로그래머스 142086: 가장 가까운 글자

def solution(s):
    answer = []
    
    for i in range(len(s)):
        temp = s[0:i].rfind(s[i]) # 일치하는 마지막 인덱스 찾기 

        if (temp == -1):
            answer.append(temp)
        else:
            answer.append(i-temp)

    return answer