# 프로그래머스 140108: 문자열 나누기

def solution(s):
    answer = 0
    same = 0
    diff = 0

    for i in range(len(s)):
        if same == 0:
            temp = s[i]
            same += 1
        else:
            if temp == s[i]:
                same += 1
            else:
                diff += 1

        
        if same == diff:
            same = 0
            diff = 0
            temp = ""
            answer += 1

        if i == len(s) - 1:
            if same != diff:
                answer += 1

    return answer