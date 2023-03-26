# 프로그래머스 43238: 입국심사

def solution(n, times):
    start = times[0] # 정답의 최솟값
    end = times[0] * n # 정답의 최댓값
    mid = (start + end) // 2

    while start < mid: # 이분 탐색
        k = 0
        for i in times:  # 해당 시간 내 입국심사를 받을 수 있는 사람의 수 카운팅
            k += mid // i
        
        if k < n:
            start = mid
        else:
            end = mid
            answer = mid # n명이 입국심사를 받을 수 있으면 정답 갱신
        mid = (start + end) // 2
            
    return answer