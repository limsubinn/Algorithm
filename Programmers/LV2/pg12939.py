# 프로그래머스 12939: 최댓값과 최솟값

def solution(s):
    num = [int(i) for i in s.split()]
    max_num = max(num)
    min_num = min(num)
    answer = str(min_num) + " " + str(max_num)
    return answer