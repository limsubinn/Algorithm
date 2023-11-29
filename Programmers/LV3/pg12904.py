# 프로그래머스 12904: 가장 긴 팰린드롬

def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            tmp = s[j:j+i] # 문자열 자르기 (길이 긴 순으로)
            if tmp == tmp[::-1]:
                return i